from django.contrib import admin
from shop.models import *


# Register your models here.
class MobileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('firm', 'name', 'price', 'quantity', 'photo')
    list_display_links = ('firm', 'name')
    list_editable = ('price', 'quantity')
    search_fields = ('name', 'firm__name')
    list_filter = ('firm',)

admin.site.register(Mobile, MobileAdmin)
admin.site.register(Firm)
