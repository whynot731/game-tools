from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Resonators)

class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('material_name', 'material_type', 'rarity')
admin.site.register(Materials, MaterialsAdmin)

class ForteCostAdmin(admin.ModelAdmin):
    #list_display = ('Resonator', 'Material', 'Target Level', 'Forte Node', 'Material Cost')
    list_display = ('resonators', 'materials', 'target_level', 'forte_node', 'stat_branch', 'node_cost')
admin.site.register(Forte_Costs, ForteCostAdmin)