from django.urls import path
from apps.ejemplares.views import ejemplarCreate, ejemplarDelete, ejemplarUpdate, listejemplar
from apps.ejemplares.views import prestarCreate, prestarDelete, prestarUpdate, listprestar
from apps.ejemplares.views import Consultas,Consultas2,Consultas3
#,Consultas3, Consultas4

app_name= 'ejemplar'
app_name= 'prestar'
urlpatterns = [
    path('', listejemplar, name= 'listejemplar'),
    path('p', listprestar, name= 'listprestar'),
    path('nuevo2/', ejemplarCreate, name= 'ejemplarCreate'),
    path('actualizar/<int:id_ejemplar>/', ejemplarUpdate, name= 'ejemplarUpdate'),
    path('eliminar/<int:id_ejemplar>/', ejemplarDelete, name= 'ejemplarDelete'),

    path('nuevooo/', prestarCreate, name= 'prestarCreate'),
    path('actualizarrr/<int:id_prestar>/', prestarUpdate, name= 'prestarUpdate'),
    path('eliminarrr/<int:id_prestar>/', prestarDelete, name= 'prestarDelete'),

    path('Consultas/', Consultas, name= 'Consultas'),
    path('Consultas2/', Consultas2, name= 'Consultas2'),
    path('Consultas3/', Consultas3, name= 'Consultas3'),
    # path('Consultas4/', Consultas4, name= 'Consultas4'),
]
