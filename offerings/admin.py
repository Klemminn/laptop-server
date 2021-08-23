from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.db.models import Q
from .models import Retailer, Offering, Scrape, Laptop, CpuFamily, CpuVendor, GpuVendor, Vendor

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('id', 'sku', 'name', 'vendor', 'cpu_model', 'ram', 'hdd', 'size', 'resolution', 'gpu_model', 'weight', 'created',)
    search_fields = ('name', 'sku', 'cpu_model', 'gpu_model',)
    list_editable = ('name', 'sku',)
    readonly_fields = ('created',)

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(CpuFamily)
class CpuFamilyAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(CpuVendor)
class CpuVendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(GpuVendor)
class GpuVendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

class OfferingIgnoredFilter(admin.SimpleListFilter):
    title = _('Ignored')

    parameter_name = 'ignored'

    def lookups(self, request, model_admin):
        return (
            ('ignored_or_inactive', _('Ignored or inactive')),
        )
    
    """Choices supplied to remove the "All" Option"""
    def choices(self, changelist):
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == _(lookup),
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        if self.value() == 'ignored_or_inactive':
            return queryset.filter(Q(ignored=True) | Q(active=False))
        return queryset.filter(ignored=False).filter(active=True)


@admin.register(Offering)
class OfferingAdmin(admin.ModelAdmin):
    list_display = ('id', 'retailer', 'sku', 'name', 'price', 'laptop', 'show_url', 'active', 'ignored', 'created',)
    list_display_links = ('id', 'name',)
    list_editable = ('ignored', 'laptop',)
    search_fields = ('name',)
    readonly_fields = ('created',)
    list_per_page = 50
    list_filter = (OfferingIgnoredFilter,)
    default_filter = ('ignored__exact=False',)

    def show_url(self, obj):
        return format_html("<a href='{url}' target='_blank'>{url}</a>", url=obj.url)

    show_url.short_description = "Url"

@admin.register(Scrape)
class ScrapeAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_offerings', 'new_offerings', 'created',)
    readonly_fields = ('created',)
