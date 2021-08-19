from django.urls import path,include
from .views import (
    FileUploadView,
    ConvertViewSet
    )



from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'convert', ConvertViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('remove-background/', FileUploadView.as_view())
]
