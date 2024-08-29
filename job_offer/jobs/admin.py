from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Job
# Register your models here.
# admin.site.register(Job)
class JobModelAdmin(admin.ModelAdmin):
    fields =('title','description','salary','expiration_date','work_hour_per_day')
    def save_model(self, request, obj, form, change):
        obj.company=request.user
        super().save_model(request, obj, form, change)
    def has_change_permission(self, request, obj=None ):
        if obj is not None:
            return obj.company==request.user
        return super().has_change_permission(request, obj)
    
    def has_delete_permission(self, request, obj= None ) :
        if obj is not None:
            return obj.company==request.user
        return super().has_delete_permission(request, obj)

admin.site.register(Job,JobModelAdmin)