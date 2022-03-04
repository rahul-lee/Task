from django.shortcuts import render
from orderapp import models
from tablib import Dataset
from rest_framework import views, permissions, response, status

# Create your views here

class AdminUpload(views.APIView):
    def post(self,request):
        data = request.data
        datafile = data.get('uploadfile')
        dataset = Dataset()
        if not datafile.name.endswith('xlsx'):
            return response.Response(
                {
            "msg": "Invalid File format",
            }, status=status.HTTP_404_NOT_FOUND
            )
        imported_data = dataset.load(datafile.read(), format='xlsx')
        for data in imported_data:
            if(models.Product.objects.filter(name=data[0]).exists()):
                pro_obj = models.Product.objects.get(name=data[0])
                pro_obj.name = data[0]
                pro_obj.price = data[1]
                pro_obj.save()
            else:
                models.Product.objects.create(name=data[0],price=int(data[1]))
        return response.Response(
                {
            "msg": "Uploaded sucessfully",
            }, status=status.HTTP_200_OK
            )
