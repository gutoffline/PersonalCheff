from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato', views.contato, name='contato'),
    path('receita/<int:receita_id>/',views.receita, name='receita')
]