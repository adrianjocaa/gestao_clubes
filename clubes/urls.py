from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('novo/', views.adicionar_clube, name='adicionar_clube'),
    path('editar/<int:clube_id>/', views.editar_clube, name='editar_clube'),
    path('excluir/<int:clube_id>/', views.excluir_clube, name='excluir_clube'),
]
