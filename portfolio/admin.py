from django.contrib import admin
from .models import Project, Skill, Experience

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ('title',)
    list_filter = ('title',)  # Add filtering by title

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')
    search_fields = ('name',)
    list_filter = ('proficiency',)  # Add filtering by proficiency

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'start_date', 'end_date')
    search_fields = ('role', 'company')
    list_filter = ('start_date', 'end_date', 'company')  # Add filtering by company
