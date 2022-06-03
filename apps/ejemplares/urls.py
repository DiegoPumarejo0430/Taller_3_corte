from django.urls import path
from apps.ejemplares.views import ejemplarCreate, ejemplarDelete, ejemplarUpdate, listejemplar
from apps.ejemplares.views import prestarCreate, prestarDelete, prestarUpdate, listprestar


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
]
