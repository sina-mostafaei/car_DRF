from django.urls import path
from .views import *
urlpatterns = [
    path('pr', pw),
    path('cr', cw),
    path('info', infu),
    path('add_frim', frim_adder),
]
