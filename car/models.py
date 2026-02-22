from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True)


class Firm(models.Model):
    title = models.CharField(max_length=20)
    membership_code = models.IntegerField()


class Car(models.Model):
    company = models.CharField(max_length=20)
    price = models.IntegerField()
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    store = models.ForeignKey(
        Firm, null=True, blank=True, on_delete=models.CASCADE)
    buyig_date=models.DateTimeField(blank=True,null=True,auto_now=True)
