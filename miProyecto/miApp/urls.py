from django.urls import path
from . import views

app_name = 'miApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('editar_producto/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('mostrar_producto/<int:pk>/', views.mostrar_producto, name='mostrar_producto'),
]
