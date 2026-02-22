from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("person_view", person_view)
router.register("car_view", car_view)
router.register("firm_view", firm_view)
router.register("info", infow,basename="cars_info")
urlpatterns = [
]

urlpatterns += router.urls
