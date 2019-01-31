
from django.urls import path

from . import views


app_name = 'Examination'

urlpatterns = [
    path('', views.index, name='index'),
]