from django.contrib import admin
from .models import Report


class ReportAdmin(admin.ModelAdmin):
    ordering = ['title']

    list_display = (
        'title',
        'comment',
        'created_at',
    )


# Register your models here.
admin.site.register(Report, ReportAdmin)
