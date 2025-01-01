from django.db import models


class VacancyDescription(models.Model):
    vacancy_name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='media/', null=True, blank=False, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.vacancy_name

    class Meta:
        verbose_name = "Описание профессии"
        verbose_name_plural = "Описания профессий"


class VacancyStatistics(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название данных ("Название вакансии")')
    table_data = models.TextField(verbose_name='Данные для таблицы')
    image = models.ImageField(upload_to='media/', null=True, blank=False, verbose_name='Изображение графика')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статистика вакансий"
        verbose_name_plural = "Статистики вакансий"
