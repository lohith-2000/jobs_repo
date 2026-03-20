from django.contrib import admin
from jobs.models import Job
# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ['company','role','status','applied_date','notes']
admin.site.register(Job, JobAdmin)