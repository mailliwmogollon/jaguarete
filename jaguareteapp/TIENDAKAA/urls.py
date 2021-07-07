from os import name
from django.urls import path
from . import views

app_name = "TIENDAKAA"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:producto_id>', views.producto, name="producto"),
    path('acerca', views.acerca, name="acerca"),
    path('contacto', views.contacto, name="contacto"),
    path('nuevo_producto', views.nuevo_producto, name="nuevo_producto"),
    path('edicion_producto/<int:producto_id>', views.edicion_producto, name="edicion_producto"),
    path('carro', views.carro, name="carro"),
    path('agregar/<int:producto_id>', views.agregar_carro, name="agregar"),
    path('busqueda', views.busqueda, name="busqueda"),
    path('filtro_categoria/<int:categoria_id>', views.filtro_categoria, name="filtro_categoria"),
    
]

