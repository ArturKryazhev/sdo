from django.urls import path,include
from . import views
app_name = 'main'

urlpatterns = [
    path('register', views.sing_up, name = 'sing_up'),
]
