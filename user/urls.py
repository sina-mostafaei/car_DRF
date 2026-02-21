from django.urls import path
from user import views
urlpatterns = [
    path('',views.create_user),
    path('profile/',views.profile)
]
