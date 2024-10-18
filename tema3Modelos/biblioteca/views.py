from django.shortcuts import render
from django.db.models import Q,F,Prefetch
from django.db.models import Avg,Max,Min
from .models import Libro,Cliente,Biblioteca

# Create your views here.
def index(request):
    return render (request, 'index.html')

def listar_libros(request):
    libros = Libro.objects.select_related("biblioteca").prefetch_related("autores")
    libros = libros.all()
    '''libros = (Libro.objects.raw("SELECT * FROM biblioteca_libro l "
                               + " JOIN biblioteca_biblioteca b ON l.biblioteca_id = b.id " 
                               + " JOIN biblioteca_libro_autores la ON la.libro_id = l.id ")
             )'''
    return render(request, 'libro.html',{"libros_mostrar":libros})

def dame_libro(request,id_libro):
    libro = Libro.objects.select_related("biblioteca").prefetch_related("autores").get(id=id_libro)
    '''libro = (Libro.objects.raw("SELECT * FROM biblioteca_libro l "
                               + " JOIN biblioteca_biblioteca b ON l.biblioteca_id = b.id " 
                               + " JOIN biblioteca_libro_autores la ON la.libro_id = l.id "
                               + " WHERE l.id = %s",[id_libro])[0]
             )'''
    return render(request, 'lista.html',{"libro_mostrar":libro})

def dame_libros_fecha(request,anyo_libro,mes_libro):
    libros = Libro.objects.prefetch_related("autores").select_related("biblioteca")
    libros = libros.filter(fecha_publicacion__year=anyo_libro,fecha_publicacion__month=mes_libro)
    """libros = (Libro.objects.raw("SELECT * FROM biblioteca_libro l "
                               + " JOIN biblioteca_libro_autores la ON la.libro_id = l.id "
                               + " JOIN biblioteca_biblioteca b ON l.biblioteca_id = b.id " 
                               + " WHERE strftime('%%Y', l.fecha_publicacion) = %s "
                               + " AND strftime('%%m', l.fecha_publicacion) = %s "
                               ,[str(anyo_libro),str(mes_libro)])
             )
    """    
    return render(request, 'libro/lista.html',{"libros_mostrar":libros})

def dame_ultimo_cliente_libro(request,libro):
    cliente= Cliente.objects.filter(prestamo__libro=libro).order_by("-prestamo__fecha_prestamo")[:1].get()
    return render(request, 'cliente/cliente.html',{"cliente":cliente})
    
