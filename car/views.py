from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import car, person, frim
from .serializers import per_ser, car_ser, frim_ser, infouw,inpho


@api_view(["GET", "POST"])
def pw(r):
    if r.method == "GET":
        persons = person.objects.all()
        prsr = per_ser(persons, many=True)
        return Response(prsr.data, status=status.HTTP_200_OK)
    elif r.method == "POST":
        ser = per_ser(data=r.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", "POST"])
def cw(r):
    if r.method == "GET":
        cars = car.objects.all()
        crsr = car_ser(cars, many=True)
        return Response(crsr.data, status=status.HTTP_200_OK)
    elif r.method == "POST":
        ser = car_ser(data=r.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def infu(r):
    cars = car.objects.all()
    crsr = infouw(cars, many=True)
    return Response(crsr.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def frim_adder(r):
    ser = frim_ser(data=r.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def infow(r):
    frims = car.objects.all()
    frms_sr = inpho(frims, many=True)
    return Response(frms_sr.data, status=status.HTTP_200_OK)