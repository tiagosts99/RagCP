from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import AccRegNum





class Purchases(admin.ModelAdmin):
    list_display = ('account_id', 'key', 'value')
    list_filter = ('account_id', 'key',)
    search_fields = ('account_id','key',)


    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset

admin.site.register(AccRegNum, Purchases)
