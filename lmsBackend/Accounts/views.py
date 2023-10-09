from django.dispatch import receiver
from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import User,Messages
from .serializers import UserModelSerializer,MessageSerializer



json = ''' 
curl -X POST http://127.0.0.1:8000/chat/ \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3MjA3Mjk1LCJpYXQiOjE2OTY4MzkyOTUsImp0aSI6IjAzNDM4ZmQ4M2IxNjQ1ZTY4ZmVmOTBjYjg1ZTdjNDkxIiwidXNlcl9pZCI6MX0.YFF2Blvi0DnA_NZ41_Q4IUQ9iZ00uWI3yF4B5hDTWF0" \
  -H "Content-Type: application/json" \
  -d '{"name": "benon"}'



 '''


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def chat_page(request):
    data= request.data
    if User.objects.filter(id=data['name']).exists():
        receiver = User.objects.get(id=data['name'])
        m = Messages(receiver = receiver,message=data['message'],sender = request.user)
        m.save()
        queryset = Messages.objects.filter(receiver = receiver,sender = request.user).all()
        serializer = MessageSerializer(queryset,many=True)
    else:  
        return Response({'message':'User Doesnot Exist'})  
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_details_settings_page(request):
    queryset = User.objects.filter(id=request.user.id) 
    serializer = UserModelSerializer(queryset,many=True)
    return Response(serializer.data)
