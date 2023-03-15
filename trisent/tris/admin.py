from django.contrib import admin
from .models import products, contact, food

# Register your models here.
admin.site.register(products)

class contactAdmin(admin.ModelAdmin):
    list_display=['name','email','subject','created_at']
    search_fields=['name','email','subject']
    list_per_page=6
admin.site.register(contact,contactAdmin)

admin.site.register(food)
