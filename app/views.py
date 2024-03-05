from django.shortcuts import render

# Create your views here.

from app.models import *
from app.serializers import *
from rest_framework.decorators import APIView
from rest_framework.response import Response


class ProductCrud(APIView):
    def get(self,request):
        PDO=Product.objects.all()
        PJD=ProductModelSerializers(PDO,many=True)
        return Response(PJD.data)
    
    def post(self,request):
        PJDO=request.data
        PDO=ProductModelSerializers(data=PJDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'Data':'Data inserted successfully'})
        else:
            return Response({'Error':'Data is not inserted'})