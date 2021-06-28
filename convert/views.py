from rest_framework import generics, status, views, permissions,viewsets
from .serializers import ConvertSerializerLoc,ConvertSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import uuid
import threading
from django.core.files.storage import FileSystemStorage
import os
from .models import Convert
from  .utils import  remove_background
# Convert.objects.filter().delete()
from pathlib import Path
from django.conf import settings
class FileUploadView(views.APIView):
    serializer_class = ConvertSerializerLoc
    queryset = Convert.objects.all()
    file_path = ''
    file_name = ''
    path = ''
    user_id = None
    convert_id = None
    def run(self,con=None):
        print(con)
        print('dd')
        convert = Convert.objects.get(pk=con)
        print(convert.file.path)
        p = Path(convert.file_name)
        print(p.stem, getattr(settings, 'MEDIA_ROOT', None))
        output_path =getattr(settings, 'MEDIA_ROOT', None)+'/removed/' + p.stem + '.PNG'

        remove_background(convert.file.path,output_path)
        convert.status = 'completed'
        convert.removed.name ='/removed/' + p.stem + '.PNG'

        convert.save()

    def post(self,request,format=None):

        files = request.FILES
        data = request.data
        print(files)
        # return Response(status=200)

        ser = ConvertSerializerLoc(data=request.data)
        if ser.is_valid():

            print(data)
            for file in files.getlist('file'):
                con = Convert.objects.create(user=data['user'], file=file,status='start',file_name=file.name,project=data['project'])
                print(con.pk)
                thread = threading.Thread(target=self.run,kwargs={'con': con.pk})
                thread.daemon = True
                thread.start()

            return Response(status=200)
        else:
            return  Response(ser.errors,
                     status=400)

class ConvertViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user','project']
    queryset = Convert.objects.all()
    serializer_class = ConvertSerializer
