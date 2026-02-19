from django.urls import path
from .views import *
urlpatterns = [
    path('pr', person_view),
    path('cr', car_view),
    path('info', car_info),
    path('add_frim', firm_adder),

]
