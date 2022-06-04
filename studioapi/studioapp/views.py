from django.shortcuts import render
from rest_framework.response import Response
from .models import MerchantInfo
from rest_framework.views import APIView
from .serializer import MerchantInfoSerializer

# Create your views here.

class MerchantInfoListAPI(APIView):
    def get(self, request):
        queryset = MerchantInfo.objects.all()
        serializer = MerchantInfoSerializer(queryset, many=True)
        return Response(serializer.data)
