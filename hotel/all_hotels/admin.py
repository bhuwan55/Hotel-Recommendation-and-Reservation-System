from django.contrib import admin
from .models import Category, Services, Hotel, Rate, Reserve, Price
# Register your models here.
admin.site.register(Category)
admin.site.register(Services)
admin.site.register(Hotel)
admin.site.register(Rate)
admin.site.register(Reserve)
admin.site.register(Price)
