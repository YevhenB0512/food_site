from django.contrib import admin

from carts.admin import CartUser
from orders.admin import OrderTabulareAdmin
from users.models import User


# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff',)
    search_fields = ('username', 'first_name', 'last_name',)
    inlines = (CartUser, OrderTabulareAdmin)