from django.urls import path
from .views import *
urlpatterns = [
    path('person_view', person_view),
    path('car_view', car_view),
    path('info', car_info),
    path('add_firm', firm_adder),

]

