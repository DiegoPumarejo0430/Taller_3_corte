from django.urls import path
from apps.libro.views import  listLibros, libroCreate, libroDelete, libroUpdate
from apps.libro.views import listautor, autorCreate, autorDelete, autorUpdate
from apps.libro.views import Consultas, Consultas2,Consultas3, Consultas4
app_name= 'libros'
app_name= 'autor'
urlpatterns = [
    path('', listLibros, name= 'listlibros'),
    path('a', listautor, name= 'listautor'),

    path('nuevo/', libroCreate, name= 'libroCreate'),
    path('actualizar/<int:id_libro>/', libroUpdate, name= 'libroUpdate'),
    path('eliminar/<int:id_libro>/', libroDelete, name= 'libroDelete'),

    path('nuevoo/', autorCreate, name= 'autorCreate'),
    path('actualizarr/<int:id_autor>/', autorUpdate, name= 'autorUpdate'),
    path('eliminarr/<int:id_autor>/', autorDelete, name= 'autorDelete'),

    path('Consultas/', Consultas, name= 'Consultas'),
    path('Consultas2/', Consultas2, name= 'Consultas2'),
    path('Consultas3/', Consultas3, name= 'Consultas3'),
    path('Consultas4/', Consultas4, name= 'Consultas4'),
    
]