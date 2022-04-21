from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import User, Inquiry
from .serializers import UserSerializer, InquirySerializer
from rest_framework import serializers
from rest_framework import status

# Create your views here.

#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('firstName')
#     serializer_class = UserSerializer
#
#
# class InquiryViewSet(viewsets.ModelViewSet):
#     queryset = Inquiry.objects.all().order_by('firstName')
#     serializer_class = InquirySerializer

# for creating new user
# class CreateUserViewSet(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# to display users
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_users': '/',
        'Search by firstName': '/?firstName=firstName',
        'Search by lastName': '/?lastName=lastName',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)

# used to add users
@api_view(['POST'])
def add_users(request):
    item = UserSerializer(data=request.data)

    # validating for already existing data
    if User.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_users(request):
    # checking for the parameters from the URL
    if request.query_params:
        items = User.objects.filter(**request.query_param.dict())
    else:
        items = User.objects.all()

    # if there is something in items else raise error
    if items:
        data = UserSerializer(items)
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_users(request, pk):
    item = User.objects.get(pk=pk)
    data = UserSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_users(request, pk):
    item = get_object_or_404(User, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
# # to update users
# class UpdateUserViewSet(generics.RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# # to delete users
# class DeleteUserViewSet(generics.DestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer



# class InquiryViewSet(viewsets.ModelViewSet):
#     queryset = Inquiry.objects.all()
#     serializer_class = InquirySerializer



