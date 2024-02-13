from django.contrib import admin
from goods.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('name', )


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'discount', 'quantity', 'category')
    list_filter = ('category', 'discount')
    list_editable = ('price', 'discount', 'quantity')
    search_fields = ('name', 'description',)
    prepopulated_fields = {'slug': ('name', )}
    fields = ('name',
              'category',
              'slug',
              'description',
              'image',
              ('price', 'discount'),
              )

