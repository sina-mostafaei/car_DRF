from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, viewsets, permissions
from .models import Car, Person, Firm
from .serializers import person_serializer, car_serializer, firm_serializer, car_info_serializer




class person_view(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = person_serializer
    http_method_names = ["post", "get"]
    search_fields = ('name',)
    ordering_fields = "__all__"




class car_view(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = car_serializer
    http_method_names = ["get", "post"]




class firm_view(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = firm_serializer
    http_method_names = ["post", "get", 'delete', "put"]



class infow(viewsets.ModelViewSet):
    search_fields = ('company',)
    ordering_fields = "__all__"
    queryset = Car.objects.all()
    http_method_names = ["post", "get", 'delete', "put"]

    def get_serializer_class(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return car_serializer
        else:
            return car_info_serializer



