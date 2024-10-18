from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('libros/listar',views.listar_libros,name='listar_libros'),
    path("libros/<int:id_libro>/", views.dame_libro,name="dame_libro"),
    path("libros/listar/<int:anyo_libro>/<int:mes_libro>", views.dame_libros_fecha,name="dame_libros_fecha"),
    path('ultimo-cliente-libro/<int:libro>',views.dame_ultimo_cliente_libro,name='ultimo_cliente_libro'),
]