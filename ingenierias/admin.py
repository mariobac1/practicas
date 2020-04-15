from django.contrib import admin
 
from ingenierias.models import IngenieriaGSM
# Register your models here.
#class ArticulosAdmin(admin.ModelAdmin):
#    search_fields=('nombre',"precio")
    
#admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(IngenieriaGSM)
