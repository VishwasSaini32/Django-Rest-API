from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework import status
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from .models import Users
from .serializers import UserSerializer

# class UserList(generics.ListCreateAPIView):
#     queryset = Users.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Users.objects.all()
#     serializer_class = UserSerializer


class UserList(APIView):
    def get(self, request, format=None):
        user = Users.objects.all()
        serializer = UserSerializer(Users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serialaizer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def user_list(request):

#     if request.method == 'GET':
#         user = Users.objects.all()
#         serializer = UserSerializer(user, many = True)
#         return Response(serializer.data)

#         elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def user_detail(request, pk):

#     try:
#         user = Users.objects.get(pk=pk)
#     except Users.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


    # @csrf_exempt
    # def user_list(request):
    #     if request.method == 'GET':
    #         users = Users.objects.all()
    #         serializer =UserSerializer(users, many=True)
    #         return JsonResponse(serializer.data, safe=False)

    #     elif request.method == 'POST':
    #         user_data = JSONParser().parse(request)
    #         serializer = UserSerializer(data=user_data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    #         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @csrf_exempt
    # def user_detail(request, pk):
    #     try:
    #         user = Users.objects.get(pk=pk)
    #     except Users.DoesNotExist:
    #         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    #     if request.method == 'GET':
    #         serializer = UserSerializer(user)
    #         return JsonResponse(serializer.data)

    #     elif request.method == 'PUT':
    #         user_data = JSONParser().parse(request)
    #         serializer = UserSerializer(user, data=user_data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data)
    #         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     elif request.method == 'DELETE':
    #         user.delete()
    #         return HttpResponse(status=status.HTTP_204_NO_CONTENT)

