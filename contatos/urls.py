from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:contato_id>', views.details, name='details'),
    path('busca/', views.busca, name='busca'),
]
