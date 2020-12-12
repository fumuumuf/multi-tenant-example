from django.contrib import admin

# Register your models here.
from tenants.models import Tenant, Domain

admin.site.register(Tenant, admin.ModelAdmin)
admin.site.register(Domain, admin.ModelAdmin)
