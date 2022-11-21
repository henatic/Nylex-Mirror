from django.urls import path
from. import views

urlpatterns = [
    path('reciever/', views.recieved)
]