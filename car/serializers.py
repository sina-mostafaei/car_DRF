from . import models as m
from rest_framework import serializers


class per_ser(serializers.ModelSerializer):
    class Meta:
        model = m.Person
        fields = "__all__"


class car_ser(serializers.ModelSerializer):
    class Meta:
        model = m.Car
        fields = "__all__"


class infouw(serializers.ModelSerializer):
    # person=m.person
    class Meta:
        model = m.Car
        fields = "__all__"
        depth = 1


class frim_ser(serializers.ModelSerializer):
    class Meta:
        model = m.Firm
        fields = "__all__"


class inpho(serializers.ModelSerializer):
    # person=m.person
    class Meta:
        model = m.Firm
        fields = "__all__"
        depth = 1
