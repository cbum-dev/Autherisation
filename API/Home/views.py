# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializer
# Create your views here.
from .serializer import TodoSerializer
@api_view(['GET','POST'])
def home(request):
        if request.method == 'GET':
            return Response(serializer.TodoSerializer)
        elif request.method == 'POST':
              return Response({
                    'status' : 'POST',
                    'message' : 'working'
              })


@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data 
        print(data)
        return Response({
             'status' : True,
             'message' : 'success!!!!!!!!!'
        })
    except Exception as e:
        print(e)
        return Response({
             'status' : False,
             'mmessage' : 'hahaha'
        })
        
         
