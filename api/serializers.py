from rest_framework import serializers
from .models import Chiste

class ChisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chiste
        fields = '__all__'