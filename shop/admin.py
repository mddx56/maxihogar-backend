from django.contrib import admin

from .models import (
    Product,
    Product_Sku,
    Product_Attribute,
    Categorie,
    Sub_Categorie,
    Product_Image,
)

admin.site.site_header = "MaxiHogar"
admin.site.site_title = "MaxiHogar Admin"
admin.site.index_title = "Bienvenidos 🏪"

"""
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "anio",
        "en_curso",
    )
    list_display_links = ("id",)
    # list_editable = ("precio", "nombre")
    search_fields = ("id", "anio")
    list_per_page = 25
"""

admin.site.register(Categorie)
admin.site.register(Sub_Categorie)
admin.site.register(Product_Attribute)
admin.site.register(Product)
admin.site.register(Product_Sku)
admin.site.register(Product_Image)
