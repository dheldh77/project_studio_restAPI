# restapp/serializer.py
from rest_framework import serializers
from .models import MerchantInfo

class MerchantInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchantInfo # 사용할 모델
        fields = '__all__' # 모든 필드 포함