from django.contrib import admin
from .models import Project, Skill, Experience, Certificate

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'repo_link')
    search_fields = ('title',)
    list_filter = ('title',) 

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')
    search_fields = ('name',)
    list_filter = ('proficiency',) 

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'start_date', 'end_date')
    search_fields = ('role', 'company')
    list_filter = ('start_date', 'end_date', 'company')  

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
