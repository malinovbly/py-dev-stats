from django.contrib import admin
from .models import (VacancyDescription,
                     SalaryLevelByYearData,
                     VacanciesCountByYearData,
                     SalaryLevelByAreaData,
                     VacanciesFractionByAreaData)


@admin.register(VacancyDescription)
class VacancyDescriptionAdmin(admin.ModelAdmin):
    list_display = ('vacancy_name', 'created_at', 'updated_at')
    search_fields = ('vacancy_name',)


@admin.register(SalaryLevelByYearData)
class SalaryLevelByYearDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(VacanciesCountByYearData)
class VacanciesCountByYearDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(SalaryLevelByAreaData)
class SalaryLevelByAreaDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(VacanciesFractionByAreaData)
class VacanciesFractionByAreaDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
