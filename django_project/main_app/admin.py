from django.contrib import admin
from .models import VacancyDescription


@admin.register(VacancyDescription)
class VacancyDescriptionAdmin(admin.ModelAdmin):
    list_display = ('vacancy_name', 'created_at', 'updated_at')
    search_fields = ('vacancy_name',)
