from rest_framework import serializers
from .models import Convert
class ConvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convert
        fields = '__all__'

class ConvertSerializerLoc(serializers.ModelSerializer):
    file = serializers.ListField(
        child=serializers.ImageField(max_length=100000,
                                    allow_empty_file=False,
                                    use_url=True)
    )

    class Meta:
        model = Convert
        fields = ('user','file')