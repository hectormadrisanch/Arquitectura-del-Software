from django.urls import path
from .views import (
    lista_clientes, 
    detalle_cliente, 
    registrar_cliente, 
    registrar_coche, 
    registrar_servicio,
    buscar_coche_por_matricula, 
    buscar_servicios_de_coche,
    buscar_cliente,          
    buscar_coches_de_cliente,
    buscar_coches_por_marca,
    coches_sin_servicios,
    nuevo_cliente,
    nuevo_coche,
    nuevo_servicio,
    contratar_servicio
)

urlpatterns = [
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('clientes/<int:cliente_id>/', detalle_cliente, name='detalle_cliente'),
    path('clientes/registrar/', registrar_cliente, name='registrar_cliente'),
    path('coches/registrar/', registrar_coche, name='registrar_coche'),
    path('servicios/registrar/', registrar_servicio, name='registrar_servicio'), 
    path('coches/matricula/<str:matricula>/', buscar_coche_por_matricula, name='buscar_coche_por_matricula'),
    path('coches/<int:coche_id>/servicios/', buscar_servicios_de_coche, name='buscar_servicios_de_coche'),
    path('clientes/<int:cliente_id>/', buscar_cliente, name='buscar_cliente'),
    path('clientes/<int:cliente_id>/coches/', buscar_coches_de_cliente, name='buscar_coches_de_cliente'),
    path('coches/marca/<str:marca>/', buscar_coches_por_marca, name='buscar_coches_por_marca'),
    path('coches/sin-servicios/', coches_sin_servicios, name='coches_sin_servicios'),
    path('clientes/nuevo/', nuevo_cliente, name='nuevo_cliente'),
    path('coches/nuevo/', nuevo_coche, name='nuevo_coche'),
    path('servicios/nuevo/', nuevo_servicio, name='nuevo_servicio'),
    path('servicios/contratar/', contratar_servicio, name='contratar_servicio'),
]