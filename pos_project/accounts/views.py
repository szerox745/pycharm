from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def login_view(request):
    """
    Vista para manejar el inicio de sesión de los usuarios.
    """
    # Si el usuario ya está autenticado, lo redirigimos a la página de inicio.
    if request.user.is_authenticated:
        return redirect('home')
    
    # Si el método de la petición es POST, significa que se envió el formulario.
    if request.method == 'POST':
        # Creamos una instancia del formulario de autenticación con los datos enviados.
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Si el formulario es válido, obtenemos el usuario.
            user = form.get_user()
            # Iniciamos la sesión para ese usuario.
            login(request, user)
            messages.success(request, f'¡Bienvenido de nuevo, {user.full_name}!')
            return redirect('home')
        else:
            # Si el formulario no es válido, mostramos un error.
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        # Si la petición es GET, simplemente mostramos un formulario vacío.
        form = AuthenticationForm()
        
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    """
    Vista para cerrar la sesión del usuario.
    """
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('login')

@login_required
def profile_view(request):
    """
    Vista para mostrar el perfil del usuario.
    """
    # Simplemente renderiza la plantilla del perfil, pasando el usuario actual.
    return render(request, 'accounts/profile.html')

@login_required
def profile_update(request):
    """
    Vista para procesar la actualización de los datos del perfil del usuario.
    """
    if request.method == 'POST':
        user = request.user
        # Actualizamos los campos del usuario con los datos del formulario.
        user.full_name = request.POST.get('full_name', user.full_name)
        user.email = request.POST.get('email', user.email)
        user.mobile = request.POST.get('mobile', user.mobile)
        user.save()
        messages.success(request, 'Perfil actualizado correctamente.')
    # Redirigimos de vuelta a la página del perfil.
    return redirect('profile')

