# admin: el módulo que arma el panel /admin automáticamente
from django.contrib import admin
# Servicio: el modelo que escribiste en el paso 02, importado desde este mismo directorio
from .models import Servicio

# register: le dice a Django "muestra este modelo en el panel /admin, con un CRUD ya armado"
#admin.site.register(Servicio)

@admin.register(Servicio)
# ServicioAdmin: clase que personaliza cómo se ve Servicio en el panel
class ServicioAdmin(admin.ModelAdmin):
    # list_display: los campos que aparecen como columnas en la lista
    list_display = ('titulo', 'categoria')