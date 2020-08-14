import jwt

from django.http import HttpResponseForbidden
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework_jwt.serializers import jwt_payload_handler


from .models import Worker
from .serializers import WorkerSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_workers(request):
    workers = Worker.objects.all()
    serializer = WorkerSerializer(workers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def auth_worker(request):
    username = request.data['username']
    password = request.data['password']

    print(f'username: {username}, password: {password}, ')

    user = authenticate(username=username, password=password)

    if user is not None:
        payload = jwt_payload_handler(user)
        token = jwt.encode(payload, settings.SECRET_KEY)

        response_model = {}
        response_model['token'] = token

        return Response(response_model, status=status.HTTP_200_OK)

    return HttpResponseForbidden()
