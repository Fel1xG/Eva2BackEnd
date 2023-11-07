from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm

def index(request):
    return render(request, 'miApp/index.html')
    
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'miApp/lista_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('miApp:lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'miApp/crear_producto.html', {'form': form})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('miApp:lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'miApp/editar_producto.html', {'form': form})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('miApp:lista_productos')
    return render(request, 'miApp/eliminar_producto.html', {'producto': producto})

def mostrar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    return render(request, 'miApp/mostrar_producto.html', {'producto': producto})

