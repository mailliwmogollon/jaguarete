from django.shortcuts import redirect, render, get_object_or_404
from .forms import *
from .models import Producto, Categoria, Carro
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "jaguareteapp/index.html", {
        "lista_principal": Producto.objects.all()[0:3],
        "lista_productos": Producto.objects.all()[3:10],
        "lista_secciones": Categoria.objects.all(),
    })

def filtro_categoria(request, categoria_id):
    una_categoria= get_object_or_404(Categoria, id=categoria_id)
    queryset = Producto.objects.all()
    queryset = queryset.filter(categoria=una_categoria)
    return render(request,"jaguareteapp/index.html", {
        "lista_articulos": queryset,
        "lista_secciones": Categoria.objects.all(),
        "seccion_seleccionada": una_categoria
    })

def busqueda(request):
    busqueda_usuario = request.GET.get("buscar")
    busqueda = Producto.objects.all() 

    if busqueda_usuario:
        busqueda = Producto.objects.filter(
            Q(titulo__icontains = busqueda_usuario)
        ).distinct()
    return render(request, "jaguareteapp/index.html", {
        "busqueda": busqueda
    })

def producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, "jaguareteapp/producto.html", {
        "producto": producto
    })

def nuevo_producto(request):

    if request.method == "POST":
        user = User.objects.get(username=request.user)
        form = FormProducto(request.POST, request.FILES, instance=Producto(imagen=request.FILES['imagen'])) 
        if form.is_valid():
            form.save()
            return redirect("TIENDAKAA:index")  
    else:
        form = FormProducto()
        return render(request, "jaguareteapp/nuevo_producto.html", {
            "form": form
        })
 
def edicion_producto(request, producto_id):
    un_producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":  
        user = User.objects.get(username=request.user)   
        form = FormProducto(data=request.POST, files=request.FILES, instance=un_producto)
        if form.is_valid():
            form.save()
            return redirect("TIENDAKAA:index")
    else:
        form = FormProducto(instance = un_producto)
        return render(request, "jaguareteapp/edicion_producto.html", {
            "producto": un_producto,
            "form": form
        })

def producto_eliminar(request, producto_id):
    un_producto = get_object_or_404(Producto, id=producto_id)
    un_producto.delete()
    return redirect("TIENDAKAA:index")

def acerca(request):
    return render(request, "jaguareteapp/acerca.html")

def contacto(request):
    return render(request, "jaguareteapp/contacto.html")

def carro(request):
    return render(request, "jaguareteapp/carro.html", {
        "lista_carro": Carro.objects.all()
    })
   

def agregar_carro(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("TIENDAKAA:carro")



