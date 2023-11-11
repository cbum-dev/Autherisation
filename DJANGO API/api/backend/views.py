from django.shortcuts import render
from .models import Cars
from .serialisers import carSerialiser
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST',"PUT","DELETE"])
def cars(request):
    if request.method == "GET":
        serializer = carSerialiser(obj,many =True)
        return Response(serializer.data) 
    elif request.method == "POST":
        data = request.data
        serializer = carSerialiser(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    return Response(serializer.error_messages)  