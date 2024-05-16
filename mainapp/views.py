from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from rest_framework.parsers import MultiPartParser

def index(request):
    return render(request, 'index.html')

def download(request,uid):
    return render(request, 'download.html', {"uid" : uid})

class Handelupload(APIView):
    parser_classes = [MultiPartParser]
    def post(self, request):
        try:
            data = request.data
            serializer = FileList(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status' : 200,
                    'message' : 'files uploaded scusses',
                    'data' : serializer.data
                })
            return Response({
                    'status' : 400,
                    'message' : 'somehing went wrong',
                    'error' : serializer.errors
                })
            
        except Exception as e:
            return Response({
                'status': 500,  
                'message': 'Internal server error occurred',
                'error': str(e)  
            })


