from django.shortcuts import render, redirect
from apps.ejemplares.form import ejemplarForm, prestarForm
from apps.ejemplares.models import Ejemplares, Prestar
from django.db.models import Count
 #Create your views here.

def listejemplar(request):
    ejemplares = Ejemplares.objects.all().order_by('-id')
    context = {'ejemplares': ejemplares}
    return render(request, 'ejemplar/listejemplar.html',context)

def listprestar(request):
    prestars = Prestar.objects.all().order_by('-id')
    context = {'prestars': prestars}
    return render(request, 'prestar/listprestar.html',context)

def home(request):
    return render(request, 'base/base.html')

def ejemplarCreate(request):
    if request.method == 'POST':
        form = ejemplarForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ejemplar:listejemplar')
    else:
        form = ejemplarForm()
    return render(request, 'ejemplar/ejemplar_form.html', {'form': form})

def prestarCreate(request):
    if request.method == 'POST':
        form = prestarForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('prestar:listprestar')
    else:
        form = prestarForm()
    return render(request, 'prestar/prestar_form.html', {'form': form})

def ejemplarUpdate(request, id_ejemplar):
    mant = Ejemplares.objects.get(pk=id_ejemplar)

    if request.method == 'GET':
        form = ejemplarForm(instance=mant)
    else:
        form = ejemplarForm(request.POST, instance=mant)
        if form.is_valid():
            form.save()
        return redirect('ejemplar:listejemplar')
    
    return render(request, 'ejemplar/ejemplar_form.html', {'form': form})

def prestarUpdate(request, id_prestar):
    mant = Prestar.objects.get(pk=id_prestar)

    if request.method == 'GET':
        form = prestarForm(instance=mant)
    else:
        form = prestarForm(request.POST, instance=mant)
        if form.is_valid():
            form.save()
        return redirect('prestar:listprestar')
    
    return render(request, 'prestar/prestar_form.html', {'form': form})

def ejemplarDelete(request, id_ejemplar):
    mant = Ejemplares.objects.get(pk=id_ejemplar)
    if request.method == 'POST':
       mant.delete()
       return redirect('ejemplar:listejemplar')
    return render(request, 'ejemplar/ejemplarDelete.html', {'ejemplar': mant})

def prestarDelete(request, id_prestar):
    mant = Prestar.objects.get(pk=id_prestar)
    if request.method == 'POST':
       mant.delete()
       return redirect('prestar:listprestar')
    return render(request, 'prestar/prestarDelete.html', {'prestar': mant})

def Consultas(request):
    ejemplar =Prestar.objects.filter(fecha_dev__range=['2022-05-01','2022-05-30']).values('user__username', 'ejemplares__libro__titulo','fecha_pres','fecha_dev')
    context = {'ejemplar': ejemplar}
    return render(request, 'ejemplar/Consultas.html',context)

def Consultas2(request):
    ejemplar = Prestar.objects.values('ejemplares__libro__titulo').annotate(total=Count('ejemplares__libro__titulo'))
    context = {'ejemplar': ejemplar}
    return render(request, 'ejemplar/Consultas2.html',context)
