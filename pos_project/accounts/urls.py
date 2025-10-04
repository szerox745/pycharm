from django.urls import path
from . import views

# Este archivo solo debe contener las URLs de la app 'accounts'.

urlpatterns = [
    # URLs para el perfil de usuario
    path('perfil/', views.profile_view, name='profile'),
    path('perfil/actualizar/', views.profile_update, name='profile_update'),
]

