from django.urls import path

from . import views

app_name = 'shortener'
urlpatterns = [path('', views.index, name='index'), path('<str:short_code>', views.parse, name='parse')]
