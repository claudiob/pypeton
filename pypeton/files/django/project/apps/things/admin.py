from things.models import Thing
from django.contrib import admin

class ThingAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'name')
    fieldsets = [
        (None,          {'fields': ['name', 'slug']}),
    ]
    prepopulated_fields = {"slug": ("name",)}
    list_filter  = ['name']

admin.site.register(Thing, ThingAdmin)

