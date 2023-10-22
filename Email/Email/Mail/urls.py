from django.urls import path,include
from .views import send_email
from Mail import views

urlpatterns = [
    path('',views.send_email,name="email"),
]
