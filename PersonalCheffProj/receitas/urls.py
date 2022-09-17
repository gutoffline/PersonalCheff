from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato', views.contato, name='contato'),
    path('sucodelaranja', views.sucodelaranja, name='sucodelaranja'),
    path('sucodelimao', views.sucodelimao, name='sucodelimao'),
]