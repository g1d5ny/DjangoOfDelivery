from django.contrib import admin
from .models import Point


class PointAdmin(admin.ModelAdmin):
    list_display = ['code', 'use_from', 'use_to', 'amount', 'active']
    list_filter = ['active', 'use_from', 'use_to']
    search_fields = ['code']


admin.site.register(Point, PointAdmin)
