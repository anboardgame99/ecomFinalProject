from django.contrib import admin
from coverage.models import *



# Register your models here.
class warrantyAdmin(admin.ModelAdmin):
    list_display = ['warranty_id', 'product_id', 'warranty_description', 'warranty_status', 'warranty_cost']


admin.site.register(Warranty, warrantyAdmin)



