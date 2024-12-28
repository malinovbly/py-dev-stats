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
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"


class SalaryLevelByYearData(models.Model):
    name = models.CharField(max_length=255, verbose_name='Данные')
    salary_lvl_by_year = models.TextField(verbose_name='Данные таблицы "Динамика уровня зарплат по годам"')
    salary_lvl_by_year_img = models.ImageField(upload_to='media/', null=True, blank=False, verbose_name='График таблицы "Динамика уровня зарплат по годам"')

    def __str__(self):
        return f'Зарплаты по годам id={self.id}'

    class Meta:
        verbose_name = "Динамика уровня зарплат по годам"
        verbose_name_plural = "Динамики уровня зарплат по годам"


class VacanciesCountByYearData(models.Model):
    name = models.CharField(max_length=255, verbose_name='Данные')
    vacs_cnt_by_year = models.TextField(verbose_name='Данные таблицы "Динамика количества вакансий по годам"')
    vacs_cnt_by_year_img = models.ImageField(upload_to='media/', null=True, blank=False, verbose_name='График таблицы "Динамика количества вакансий по годам"')

    def __str__(self):
        return f'Количество вакансий по годам id={self.id}'

    class Meta:
        verbose_name = "Динамика количества вакансий по годам"
        verbose_name_plural = "Динамики количества вакансий по годам"


class SalaryLevelByAreaData(models.Model):
    name = models.CharField(max_length=255, verbose_name='Данные')
    salary_lvl_by_area = models.TextField(verbose_name='Данные таблицы "Уровень зарплат по городам"')
    salary_lvl_by_area_img = models.ImageField(upload_to='media/', null=True, blank=False, verbose_name='График таблицы "Уровень зарплат по городам"')

    def __str__(self):
        return f'Зарплаты по городам id={self.id}'

    class Meta:
        verbose_name = "Уровень зарплат по городам"
        verbose_name_plural = "Уровни зарплат по городам"


class VacanciesFractionByAreaData(models.Model):
    name = models.CharField(max_length=255, verbose_name='Данные')
    vacs_frac_by_area = models.TextField(verbose_name='Данные таблицы "Доля вакансий по городам"')
    vacs_frac_by_area_img = models.ImageField(upload_to='media/', null=True, blank=False, verbose_name='График таблицы "Доля вакансий по городам"')

    def __str__(self):
        return f'Доли вакансий по городам id={self.id}'

    class Meta:
        verbose_name = "Доля вакансий по городам"
        verbose_name_plural = "Доли вакансий по городам"
