from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("", create_user, basename="temp1")

urlpatterns = [
    path('profile/', profile)
]


urlpatterns += router.urls
