from django.shortcuts import render

# Create your views here.

from app.models import *
from app.serializers import *
from rest_framework.decorators import APIView
from rest_framework.response import Response


class ProductCrud(APIView):

# get method is used for creating the objects

    def get(self,request,Pro_id):
        #PDO=Product.objects.all()
        #PJD=ProductModelSerializers(PDO,many=True)

        PDO=Product.objects.get(Pro_id=Pro_id)
        PJD=ProductModelSerializers(PDO)
        return Response(PJD.data)

# post method is used for Insert the objects into the Database 
    def post(self,request):
        PJDO=request.data
        PDO=ProductModelSerializers(data=PJDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'Data':'Data inserted successfully'})
        else:
            return Response({'Error':'Data is not inserted'})


# put method is used for updating the objects.
# if you want update the one column also it needs the all the columns if it is(non-updated column also),otherwise it throw error   
    def put(self,request,Pro_id):
        PO=Product.objects.get(Pro_id=Pro_id)
        PDO=ProductModelSerializers(PO,data=request.data)
        if PDO.is_valid():
            PDO.save()
            return Response({'Update':'Data is Updated Successfully'})
        
        else:
            return Response({'Error':'Data is not Updated'})


# patch method is used for updating the objects.
# if you want update the one column we can give non-updated column also, it doesn't throw any error   
    def patch(self,request,Pro_id):
        PO=Product.objects.get(Pro_id=Pro_id)
        PDO=ProductModelSerializers(PO,data=request.data,partial=True) #Partial is used for allows to updating the some columns 
        
        if PDO.is_valid():
            PDO.save()
            return Response({'Update':'Data is Updated Successfully'})
        
        else:
            return Response({'Error':'Data is not Updated'})


# Delete is used for deleting the product
    def delete(self,request,Pro_id):
        Product.objects.get(Pro_id=Pro_id).delete()
        return Response ({'Delete':'Data is Deleted Successfully'})
