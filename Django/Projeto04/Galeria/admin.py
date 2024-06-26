from django.contrib import admin
from Galeria.models import Fotografia

class ListandoFotografia(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("nome",)
    list_editable = ("publicada",)
    list_per_page = 10
admin.site.register(Fotografia, ListandoFotografia)
