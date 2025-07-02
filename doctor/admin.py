from django.contrib import admin
from .models import Designation,Specialization,Doctor,AvailableTime,Review

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',),}
    
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',),}

admin.site.register(Designation,DesignationAdmin)
admin.site.register(Specialization,SpecializationAdmin)
admin.site.register(AvailableTime)
admin.site.register(Doctor)
admin.site.register(Review)