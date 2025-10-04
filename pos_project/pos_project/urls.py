from django.contrib import admin
from django.urls import path, include
# Estas dos importaciones son necesarias para los archivos estáticos
from django.conf import settings
from django.conf.urls.static import static

from core.views import home
from accounts.views import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    # --- LÍNEAS YA NO COMENTADAS ---
    path('accounts/', include('accounts.urls')),
    path('core/', include('core.urls')),
]

# --- ESTE BLOQUE ES LA SOLUCIÓN ---
# Le dice a Django cómo servir los archivos de las carpetas 'static' y 'media'
# solo cuando estamos en modo de desarrollo (DEBUG = True).
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

