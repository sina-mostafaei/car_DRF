from django.db import models

# Create your models here.


class person(models.Model):
    name = models.CharField(max_length=30)
    moobile = models.IntegerField()
    date = models.DateTimeField(auto_now=True, auto_now_add=False)


class frim(models.Model):
    title=models.CharField(max_length=20)
    membership_code=models.IntegerField()

class car(models.Model):
    company = models.CharField(max_length=20)
    price = models.IntegerField()
    owner = models.ForeignKey(person, on_delete=models.CASCADE)
    store = models.ForeignKey(frim, null=True,blank=True,on_delete=models.CASCADE)