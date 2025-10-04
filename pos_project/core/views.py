from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import uuid
# Se han corregido las importaciones para ser absolutas y evitar errores del editor.
from core.models import Articulo, GrupoArticulo, LineaArticulo, ListaPrecio
from core.forms import ArticuloForm, ListaPrecioForm
from django.contrib.auth import get_user_model

from django.http import JsonResponse
from .models import LineaArticulo

Usuario = get_user_model()

@login_required
def home(request):
    """Vista para la página principal (dashboard)."""
    total_articulos = Articulo.objects.count()
    total_usuarios = Usuario.objects.count()
    bajo_stock = Articulo.objects.filter(stock__lt=10).count()
    context = {
        'total_articulos': total_articulos,
        'total_usuarios': total_usuarios,
        'bajo_stock': bajo_stock,
        'ventas_hoy': 0, # Dato simulado
    }
    return render(request, 'core/index.html', context)

@login_required
def articulos_list(request):
    """Vista para listar artículos con paginación."""
    articulos_list = Articulo.objects.select_related('grupo', 'linea', 'listaprecio').all().order_by('descripcion')
    paginator = Paginator(articulos_list, 15) # 15 artículos por página
    page_number = request.GET.get('page')
    articulos = paginator.get_page(page_number)
    return render(request, 'core/articulos/list.html', {'articulos': articulos})

@login_required
def articulo_detail(request, articulo_id):
    """Vista para ver el detalle de un artículo."""
    articulo = get_object_or_404(Articulo, articulo_id=articulo_id)
    return render(request, 'core/articulos/detail.html', {'articulo': articulo})

@login_required
def articulo_create(request):
    """Vista para crear un nuevo artículo."""
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        precio_form = ListaPrecioForm(request.POST)
        if form.is_valid() and precio_form.is_valid():
            articulo = form.save(commit=False)
            articulo.articulo_id = uuid.uuid4()
            articulo.save()
            
            lista_precio = precio_form.save(commit=False)
            lista_precio.articulo = articulo
            lista_precio.save()
            
            messages.success(request, 'Artículo creado correctamente.')
            return redirect('articulo_detail', articulo_id=articulo.articulo_id)
    else:
        form = ArticuloForm()
        precio_form = ListaPrecioForm()
    return render(request, 'core/articulos/form.html', {'form': form, 'precio_form': precio_form})

@login_required
def articulo_edit(request, articulo_id):
    """Vista para editar un artículo existente."""
    articulo = get_object_or_404(Articulo, articulo_id=articulo_id)
    lista_precio, created = ListaPrecio.objects.get_or_create(articulo=articulo)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, instance=articulo)
        precio_form = ListaPrecioForm(request.POST, instance=lista_precio)
        if form.is_valid() and precio_form.is_valid():
            form.save()
            precio_form.save()
            messages.success(request, 'Artículo actualizado correctamente.')
            return redirect('articulo_detail', articulo_id=articulo.articulo_id)
    else:
        form = ArticuloForm(instance=articulo)
        precio_form = ListaPrecioForm(instance=lista_precio)
    return render(request, 'core/articulos/form.html', {'form': form, 'precio_form': precio_form})

@login_required
def articulo_delete(request, articulo_id):
    """Vista para eliminar un artículo."""
    articulo = get_object_or_404(Articulo, articulo_id=articulo_id)
    # En un caso real, aquí iría una página de confirmación.
    # Por simplicidad en la guía, eliminamos directamente.
    articulo.delete()
    messages.success(request, 'Artículo eliminado correctamente.')
    return redirect('articulos_list')


@login_required
def get_lineas_por_grupo(request, grupo_id):
    """API simple para obtener líneas de artículo para AJAX."""
    lineas = LineaArticulo.objects.filter(grupo_id=grupo_id, estado=1).values('linea_id', 'nombre_linea')
    return JsonResponse(list(lineas), safe=False)

def cargar_lineas(request):
    grupo_id = request.GET.get('grupo_id')
    lineas = LineaArticulo.objects.filter(grupo_id=grupo_id, estado=1).order_by('nombre_linea')  # 1 = ACTIVO
    data = [{'id': linea.pk, 'nombre': linea.nombre_linea} for linea in lineas]
    return JsonResponse(data, safe=False)