from django.contrib import admin
from .models import registros

class registrosAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_entrada",)

# Register your models here.
admin.site.register(registros, registrosAdmin)