from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(BarInventoryItem)
admin.site.register(BarInventoryProduct)
admin.site.register(Purchase)
admin.site.register(ProductCategory)
admin.site.register(Brands)
admin.site.register(PurchaseItem)
