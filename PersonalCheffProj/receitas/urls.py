from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sucodelaranja', views.sucodelaranja, name='sucodelaranja'),
]