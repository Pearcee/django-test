from django.contrib import admin
from projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Project, ProjectAdmin)


