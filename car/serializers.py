from . import models as m
from rest_framework import serializers


class person_serializer(serializers.ModelSerializer):
    class Meta:
        model = m.Person
        fields = "__all__"


class car_serializer(serializers.ModelSerializer):
    class Meta:
        model = m.Car
        fields = "__all__"


        


class firm_serializer(serializers.ModelSerializer):
    class Meta:
        model = m.Firm
        fields = "__all__"


class firm_info_serializr(serializers.ModelSerializer):
    
    class Meta:
        model = m.Firm
        fields = "__all__"

        

class car_info_serializer(serializers.ModelSerializer):
    class Meta:
        model = m.Car
        fields = "__all__"
    owner=person_serializer(read_only=True)
    store=firm_serializer(read_only=True)
