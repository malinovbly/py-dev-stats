from django.contrib import admin
from .models import (VacancyDescription,
                     VacancyStatistics)


@admin.register(VacancyDescription)
class VacancyDescriptionAdmin(admin.ModelAdmin):
    list_display = ('vacancy_name', 'created_at', 'updated_at')
    search_fields = ('vacancy_name',)


@admin.register(VacancyStatistics)
class VacancyStatisticsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
