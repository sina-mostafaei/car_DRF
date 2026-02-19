from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Car, Person, Firm
from .serializers import person_serializer, car_serializer, firm_serializer, car_info_serializer, firm_info_serializr


@api_view(["GET", "POST"])
def person_view(r):
    if r.method == "GET":
        persons = Person.objects.all()
        prsr = person_serializer(persons, many=True)
        return Response(prsr.data, status=status.HTTP_200_OK)
    elif r.method == "POST":
        ser = person_serializer(data=r.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", "POST"])
def car_view(r):
    if r.method == "GET":
        cars = Car.objects.all()
        crsr = car_serializer(cars, many=True)
        return Response(crsr.data, status=status.HTTP_200_OK)
    elif r.method == "POST":
        ser = car_serializer(data=r.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def car_info(r):
    cars = Car.objects.all()
    crsr = car_info_serializer(cars, many=True)
    return Response(crsr.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def firm_adder(r):
    ser = firm_serializer(data=r.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def firm_info(r):
    firms = Car.objects.all()
    frms_sr = firm_info_serializr(firms, many=True)
    return Response(frms_sr.data, status=status.HTTP_200_OK)
