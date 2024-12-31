from django.shortcuts import render
from .models import (VacancyDescription,
                     SalaryLevelByYearData,
                     VacanciesCountByYearData,
                     SalaryLevelByAreaData,
                     VacanciesFractionByAreaData, Top20KeySkillsByYearData)


def index(request):
    content = VacancyDescription.objects.first()
    return render(request, 'index.html', {'content': content})


def general_statistics(request):
    # Динамика уровня зарплат по годам
    salary_by_year_data = SalaryLevelByYearData.objects.first()
    data1 = salary_by_year_data.salary_lvl_by_year.replace('\r\n', ' ').split(', ')
    salary_by_year_table = [d.split(': ') for d in data1]
    for d in salary_by_year_table:
        d[1] = '{0:,}'.format(float(d[1])).replace(',', ' ')
        if (len(d[1]) - d[1].find('.') - 1) < 2:
            d[1] += '0'

    # Динамика количества вакансий по годам
    vacancies_count_by_year_data = VacanciesCountByYearData.objects.first()
    data2 = vacancies_count_by_year_data.vacs_cnt_by_year.replace('\r\n', ' ').split(', ')
    vacancies_count_by_year_table = [d.split(': ') for d in data2]
    for d in vacancies_count_by_year_table:
        d[1] = '{0:,}'.format(int(d[1])).replace(',', ' ')

    # Уровень зарплат по городам (в порядке убывания)
    salary_by_area_data = SalaryLevelByAreaData.objects.first()
    data3 = salary_by_area_data.salary_lvl_by_area.replace('\r\n', ' ').split(', ')
    salary_by_area_table = [d.split(': ') for d in data3]
    for d in salary_by_area_table:
        d[1] = '{0:,}'.format(float(d[1])).replace(',', ' ')
        if (len(d[1]) - d[1].find('.') - 1) < 2:
            d[1] += '0'

    # Доля вакансий по городам
    vacancies_fraction_by_area_data = VacanciesFractionByAreaData.objects.first()
    data4 = vacancies_fraction_by_area_data.vacs_frac_by_area.replace('\r\n', ' ').split(', ')
    vacancies_fraction_by_area_table = [d.split(': ') for d in data4]
    for d in vacancies_fraction_by_area_table:
        if (len(d[1]) - d[1].find('.') - 1) < 3:
            d[1] += '0'
        percentage = round(float(d[1]) * 100, 2)
        d.append(f'{percentage}%')


    # Топ-20 навыков по годам
    top_20_key_skills_by_year_data = Top20KeySkillsByYearData.objects.first()
    data5 = top_20_key_skills_by_year_data.top_20_key_skills_by_year.replace('\r\n', ' ').split(', ')
    top_20_key_skills_by_year_table = [d.split(': ') for d in data5]
    skills_count = sum([int(d[1]) for d in top_20_key_skills_by_year_table])
    for d in top_20_key_skills_by_year_table:
        d[1] = str(round(int(d[1]) / skills_count, 3))
        if (len(d[1]) - d[1].find('.') - 1) < 3:
            d[1] += '0'
        percentage = round(float(d[1]) * 100, 2)
        d.append(f'{percentage}%')

    print()

    top_20_key_skills_by_year_table = sorted(top_20_key_skills_by_year_table, key=lambda x: x[1], reverse=True)

    return render(
        request,
        'general-statistics.html',
        {
            'salary_by_year_data': salary_by_year_data,
            'salary_by_year_table': salary_by_year_table,
            'vacancies_count_by_year_data': vacancies_count_by_year_data,
            'vacancies_count_by_year_table': vacancies_count_by_year_table,
            'salary_by_area_data': salary_by_area_data,
            'salary_by_area_table': salary_by_area_table,
            'vacancies_fraction_by_area_data': vacancies_fraction_by_area_data,
            'vacancies_fraction_by_area_table': vacancies_fraction_by_area_table,
            'top_20_key_skills_by_year_data': top_20_key_skills_by_year_data,
            'top_20_key_skills_by_year_table': top_20_key_skills_by_year_table
        }
    )


def demand(request):
    vacancy_name = VacancyDescription.objects.first().vacancy_name

    return render(
        request,
        'demand.html',
        {
            'vacancy_name': vacancy_name,
        }
    )


def geography(request):
    vacancy_name = VacancyDescription.objects.first().vacancy_name

    return render(
        request,
        'geography.html',
        {
            'vacancy_name': vacancy_name,
        }
    )


def skills(request):
    return render(request, 'skills.html')


def latest_vacancies(request):
    return render(request, 'latest-vacancies.html')
