"""productly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# path se utiliza para definir rutas URL y include se utiliza para incluir las URL de otras aplicaciones.
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Define la ruta URL para acceder a las URLs de la aplicación "productos".
    # Cuando accedes a http://tu-sitio.com/productos/, las URLs definidas en el
    # archivo productos.urls serán incluidas y manejadas por esta ruta.
    path('productos/', include('productos.urls')),
]
