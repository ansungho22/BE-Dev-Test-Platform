from rest_framework import  serializers
from .models import Instagram


class InstagramSerializer(serializers.ModelSerializer):
    UploadTime = serializers.DateTimeField(read_only=True)
    title = serializers.CharField(max_length=20)
    context = serializers.CharField()
    images = serializers.URLField(read_only=True)

    class Meta:
        model = Instagram
        fields = '__all__'