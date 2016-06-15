# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
# from django.http import HttpResponse
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from rest_framework import status
from rest_framework import views
from rest_framework.response import Response
from HearthDeepApi.models import HearthLog
from HearthDeepApi.serializers import HearthLogSerializer, UserSerializer
from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.parsers import FileUploadParser
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework import permissions



class HearthLogList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = HearthLog.objects.all()
    serializer_class = HearthLogSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class HearthLogDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = HearthLog.objects.all()
    serializer_class = HearthLogSerializer

# class LogUploadList(generics.ListCreateAPIView):
#     queryset = LogUpload.objects.all()
#     serializer_class = LogUploadSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
# class LogUploadDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = LogUpload.objects.all()
#     serializer_class = LogUploadSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class LogUploadViewSet(ModelViewSet):
#     queryset = LogUpload.objects.all()
#     serializer_class = LogUploadSerializer
#     def pre_save(self, obj):
#         obj.datafile = self.request.FILES.get('file')
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user, datafile=self.request.data.get('datafile'))





# class FileLogUploadView(views.APIView):
#     parser_classes = (FileUploadParser,)
#
#     def post(self, request, filename, format=None):
#         # file_obj = request.FILES['file']
#
#         # do some stuff with uploaded file
#         return Response(status=204)


# @api_view(['GET', 'POST'])
# def hearthLog_list(request, format=None):
#     if request.method == 'GET':
#         hearthLog = HearthLog.objects.all()
#         serializer = HearthLogSerializer(hearthLog, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = HearthLogSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer, data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def hearthLog_detail(request, id, format=None):
#     try:
#         hearthLog = HearthLog.objects.get(id=id)
#     except HearthLogSerializer.DoesNotExist:
#         return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'GET':
#         serializer = HearthLogSerializer(hearthLog)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = HearthLogSerializer(hearthLog, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         hearthLog.delete()
#         return HttpResponse(status=status.HTTP_204_NO_)
