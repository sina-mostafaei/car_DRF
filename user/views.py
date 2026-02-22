from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny ,IsAuthenticated
from .serializers import user_serializer
from django.contrib.auth.models import User
from .permissions import is_owner
@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(r):
    ser=user_serializer(data=r.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data,status=status.HTTP_200_OK)
    else:
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['get'])
@permission_classes([IsAuthenticated,is_owner])
def profile(r):
    try:
        user=User.objects.get(username=r.query_params('username'))
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        ser=user_serializer(user)
        return Response(ser.data,status=status.HTTP_200_OK)
