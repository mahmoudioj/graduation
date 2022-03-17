from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CompanyMaterialPricing)
class CompanyMaterialPricingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Material)
class MaterialAdmin(admin.ModelAdmin):
    pass
