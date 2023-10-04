from rest_framework import serializers
from .models import LikeRecord

class LikeRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeRecord
        fields = '__all__'
