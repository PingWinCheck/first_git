from django.contrib import admin
from shop.models import Mobile


# Register your models here.
class ss(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'price')}


admin.site.register(Mobile, ss)
