from django.shortcuts import render
from .serializers import Carserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Carlist
from rest_framework import status

@api_view(['GET', 'POST'])
def car_list_view(request):

    if request.method=='GET':
            car = Carlist.objects.all()
            serializer = Carserializer(car, many=True)
            return Response(serializer.data)
    
    if request.method=='POST':
         serializer = Carserializer(data=request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
         
         else:
              return Response(serializer.errors)



@api_view(['GET', 'PUT', 'DELETE'])
def car_detail_view(request, pk):
    if request.method=='GET':
        try:

            car = Carlist.objects.get(pk=pk)

        except:
             return Response({'Error':'car not found'}, status=status.HTTP_404_NOT_FOUND)   
             
        serializer = Carserializer(car)
        return Response(serializer.data)
    
    if request.method == 'PUT':

         
        car = Carlist.objects.get(pk=pk)
        serializer= Carserializer(car, data = request.data)
        if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
        else:
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
         
        car = Carlist.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

             

         


         

