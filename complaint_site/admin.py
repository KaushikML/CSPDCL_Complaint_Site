from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","bp")
    search_fields = ("first_name","last_name")
    list_filter = ("date","complaint")
    ordering = ("date", )
    readonly_fields = ("complaint", )



admin.site.register(Form,FormAdmin)



