from django.contrib import admin
from .models import Portafolio
# Register your models here.

class PortafolioAdmin(admin.ModelAdmin):
   readonly_fields = ('created_at',)

admin.site.register(Portafolio,PortafolioAdmin)
