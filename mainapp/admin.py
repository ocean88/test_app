# mainapp/admin.py
from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import RetailNetwork, Entrepreneur


class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'supplier_link', 'debt_to_factory')
    list_filter = ('city',)

    def supplier_link(self, obj):
        if obj.factory:
            return mark_safe(
                f'<a href="{reverse("admin:electric_shop_factory_change", args=(obj.factory.pk,))}">{obj.factory.name}</a>')
        return '-'

    supplier_link.short_description = 'Supplier'

    @admin.action(description='Clear debt to factory')
    def clear_debt_to_factory(self, request, queryset):
        queryset.update(debt_to_factory=0)


class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'supplier_link', 'debt_to_supplier')
    list_filter = ('city',)

    def supplier_link(self, obj):
        if obj.retail_network:
            return mark_safe(
                f'<a href="{reverse("admin:electric_shop_retailnetwork_change", args=(obj.retail_network.pk,))}">{obj.retail_network.name}</a>')
        elif obj.factory:
            return mark_safe(
                f'<a href="{reverse("admin:electric_shop_factory_change", args=(obj.factory.pk,))}">{obj.factory.name}</a>')
        return '-'

    supplier_link.short_description = 'Supplier'

    @admin.action(description='Clear debt to supplier')
    def clear_debt_to_supplier(self, request, queryset):
        queryset.update(debt_to_supplier=0)


admin.site.register(RetailNetwork, RetailNetworkAdmin)
admin.site.register(Entrepreneur, EntrepreneurAdmin)
