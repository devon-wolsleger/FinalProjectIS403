from django.contrib import admin

# Register your models here.
from .models import Tenant, Admin, Apartments


admin.site.register(Tenant)
admin.site.register(Admin)
admin.site.register(Apartments)