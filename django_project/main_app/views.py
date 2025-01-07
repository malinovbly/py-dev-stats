from django.shortcuts import render
from .models import (VacancyDescription,
                     VacancyStatistics)

import bs4
import requests
from datetime import datetime, timedelta


def index(request):
    content = VacancyDescription.objects.get(vacancy_name='Python-программист')
    return render(request, 'index.html', {'content': content})


def general_statistics(request):
    salary_by_year_data, salary_by_year_table = get_stats('Динамика уровня зарплат по годам')
    salary_by_year_table = reformat_values(salary_by_year_table, float)

    vacancies_count_by_year_data, vacancies_count_by_year_table = get_stats('Динамика количества вакансий по годам')
    vacancies_count_by_year_table = reformat_values(vacancies_count_by_year_table, int)

    salary_by_area_data, salary_by_area_table = get_stats('Уровень зарплат по городам')
    salary_by_area_table = reformat_values(salary_by_area_table, float)

    vacancies_fraction_by_area_data, vacancies_fraction_by_area_table = get_stats('Доля вакансий по городам')
    vacancies_fraction_by_area_table = reformat_values(vacancies_fraction_by_area_table, float, 3, True)

    top_20_key_skills_by_year_data, top_20_key_skills_by_year_table = get_stats('Топ-20 навыков по годам')
    top_20_key_skills_by_year_table = reformat_values(top_20_key_skills_by_year_table, float, 3, True)

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
    vacancy_name = VacancyDescription.objects.get(vacancy_name='Python-программист').vacancy_name

    salary_by_year_data, salary_by_year_table = get_stats('Динамика уровня зарплат по годам', vacancy_name)
    salary_by_year_table = reformat_values(salary_by_year_table, float)

    vacancies_count_by_year_data, vacancies_count_by_year_table = get_stats('Динамика количества вакансий по годам', vacancy_name)
    vacancies_count_by_year_table = reformat_values(vacancies_count_by_year_table, int)

    return render(
        request,
        'demand.html',
        {
            'vacancy_name': vacancy_name,
            'salary_by_year_data': salary_by_year_data,
            'salary_by_year_table': salary_by_year_table,
            'vacancies_count_by_year_data': vacancies_count_by_year_data,
            'vacancies_count_by_year_table': vacancies_count_by_year_table
        }
    )


def geography(request):
    vacancy_name = VacancyDescription.objects.get(vacancy_name='Python-программист').vacancy_name

    salary_by_area_data, salary_by_area_table = get_stats('Уровень зарплат по городам', vacancy_name)
    salary_by_area_table = reformat_values(salary_by_area_table, float)

    vacancies_fraction_by_area_data, vacancies_fraction_by_area_table = get_stats('Доля вакансий по городам', vacancy_name)
    vacancies_fraction_by_area_table = reformat_values(vacancies_fraction_by_area_table, float, 3, True)

    return render(
        request,
        'geography.html',
        {
            'vacancy_name': vacancy_name,
            'salary_by_area_data': salary_by_area_data,
            'salary_by_area_table': salary_by_area_table,
            'vacancies_fraction_by_area_data': vacancies_fraction_by_area_data,
            'vacancies_fraction_by_area_table': vacancies_fraction_by_area_table
        }
    )


def skills(request):
    vacancy_name = VacancyDescription.objects.get(vacancy_name='Python-программист').vacancy_name

    top_20_key_skills_by_year_data, top_20_key_skills_by_year_table = get_stats('Топ-20 навыков по годам', vacancy_name)
    top_20_key_skills_by_year_table = reformat_values(top_20_key_skills_by_year_table, float, 3, True)

    return render(
        request,
        'skills.html',
        {
            'vacancy_name': vacancy_name,
            'top_20_key_skills_by_year_data': top_20_key_skills_by_year_data,
            'top_20_key_skills_by_year_table': top_20_key_skills_by_year_table
        }
    )


def latest_vacancies(request):
    vacancy_name = VacancyDescription.objects.get(vacancy_name='Python-программист').vacancy_name

    hh_api = 'https://api.hh.ru/vacancies'
    params = {
        'text': 'name:(Python-программист OR python OR питон OR пайтон)',
    }

    response = requests.get(hh_api, params=params)
    latest_vacs = [vac for vac in response.json().get('items', [])]
    latest_vacs = sorted(latest_vacs, key=lambda x: x['published_at'], reverse=True)[:10]

    now = datetime.now().astimezone()
    yesterday = now - timedelta(days=1)

    recent_vacs = []
    for vac in latest_vacs:
        vac_date = datetime.strptime(vac['published_at'], '%Y-%m-%dT%H:%M:%S%z')
        if yesterday <= vac_date <= now:
            recent_vacs.append({
                'name': vac['name'],
                'description': get_description(vac, hh_api),
                'key_skills': get_key_skills(vac, hh_api),
                'employer': vac['employer']['name'],
                'salary': get_salary(vac),
                'area_name': vac['area']['name'],
                'published_at': vac['published_at']
            })

    return render(
        request,
        'latest-vacancies.html',
        {
            'vacancy_name': vacancy_name,
            'recent_vacs': recent_vacs
        }
    )


##################
# Util functions #
##################

def get_stats(data_name, vacancy_name='Все вакансии'):
    data = VacancyStatistics.objects.get(name=f'{data_name} ({vacancy_name})')
    table = [
        d.split(': ') for d in data.table_data.replace('\r\n', ' ').split(', ')
    ]
    return data, table


def reformat_values(table, value_type, digits=2, add_percentage=False):
    for d in table:
        d[1] = '{0:,}'.format(value_type(d[1])).replace(',', ' ')
        if value_type == float and (len(d[1]) - d[1].find('.') - 1) < digits:
            d[1] += '0'
        if add_percentage:
            percentage = round(float(d[1]) * 100, 2)
            d.append(f'{percentage}%')
    return table


def get_description(vac, hh_api):
    return  requests.get(f"{hh_api}/{vac['id']}?host=hh.ru").json()['description']


def get_key_skills(vac, hh_api):
    result = []
    for skill in requests.get(f"{hh_api}/{vac['id']}?host=hh.ru").json()['key_skills']:
        result.append(skill['name'])
    if len(result) == 0:
        return '-'
    return ', '.join(result)


def get_salary(vac):
    result = '-'
    if vac['salary']:
        cb_api = 'https://www.cbr.ru/scripts/XML_daily.asp'
        date = f"01/{vac['published_at'][5:7]}/{vac['published_at'][:4]}"
        data = requests.get(f"{cb_api}?date_req={date}")
        soup = bs4.BeautifulSoup(data.content, 'xml')

        value = 1
        if vac['salary']['currency']:
            for valute in soup.find_all('Valute'):
                if valute.find('CharCode').text == vac['salary']['currency']:
                    value = float(valute.find('VunitRate').text.replace(',', '.'))
                    break
        salary_from = round(value * vac['salary']['from'], 2) if vac['salary']['from'] else None
        salary_to = round(value * vac['salary']['to'], 2) if vac['salary']['to'] else None

        if salary_from and salary_to:
            result = f'{salary_from} - {salary_to} ₽'
        elif salary_from and not salary_to:
            result = f'{salary_from} ₽'
        elif salary_to and not salary_from:
            result = f'{salary_to} ₽'

    return result
