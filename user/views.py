from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import user_serializer
from django.contrib.auth.models import User


@permission_classes([AllowAny])
class create_user(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = user_serializer
    http_method_names = ["post"]

    def create(self, request):
        ser = self.get_serializer(data=request.data)
        if ser.is_valid():
            item = ser.save()
            return Response(item, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['get'])
@permission_classes([IsAuthenticated])
def profile(r):
    print(r.user.username)
    if r.user.is_superuser:
        print("it's superuser")
        users = User.objects.all()
        ser = user_serializer(users, many=True)
        return Response(ser.data, status=status.HTTP_302_FOUND)
    else:

        try:
            user = User.objects.get(username=r.user.username)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            user = User.objects.get(username=str(r.user.username))
            ser = user_serializer(user)
            return Response(ser.data, status=status.HTTP_200_OK)
