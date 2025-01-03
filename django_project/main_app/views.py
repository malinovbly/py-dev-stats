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
    # Динамика уровня зарплат по годам
    salary_by_year_data = VacancyStatistics.objects.get(name='Динамика уровня зарплат по годам (Все вакансии)')
    salary_by_year_table = [
        d.split(': ') for d in salary_by_year_data.table_data.replace('\r\n', ' ').split(', ')
    ]
    for d in salary_by_year_table:
        d[1] = '{0:,}'.format(float(d[1])).replace(',', ' ')
        if (len(d[1]) - d[1].find('.') - 1) < 2:
            d[1] += '0'

    # Динамика количества вакансий по годам
    vacancies_count_by_year_data = VacancyStatistics.objects.get(name='Динамика количества вакансий по годам (Все вакансии)')
    vacancies_count_by_year_table = [
        d.split(': ') for d in vacancies_count_by_year_data.table_data.replace('\r\n', ' ').split(', ')
    ]
    for d in vacancies_count_by_year_table:
        d[1] = '{0:,}'.format(int(d[1])).replace(',', ' ')

    # Уровень зарплат по городам (в порядке убывания)
    salary_by_area_data = VacancyStatistics.objects.get(name='Уровень зарплат по городам (Все вакансии)')
    salary_by_area_table = [
        d.split(': ') for d in salary_by_area_data.table_data.replace('\r\n', ' ').split(', ')
    ]
    for d in salary_by_area_table:
        d[1] = '{0:,}'.format(float(d[1])).replace(',', ' ')
        if (len(d[1]) - d[1].find('.') - 1) < 2:
            d[1] += '0'

    # Доля вакансий по городам
    vacancies_fraction_by_area_data = VacancyStatistics.objects.get(name='Доля вакансий по городам (Все вакансии)')
    vacancies_fraction_by_area_table = [
        d.split(': ') for d in vacancies_fraction_by_area_data.table_data.replace('\r\n', ' ').split(', ')
    ]
    for d in vacancies_fraction_by_area_table:
        if (len(d[1]) - d[1].find('.') - 1) < 3:
            d[1] += '0'
        percentage = round(float(d[1]) * 100, 2)
        d.append(f'{percentage}%')


    # Топ-20 навыков по годам
    top_20_key_skills_by_year_data = VacancyStatistics.objects.get(name='Топ-20 навыков по годам (Все вакансии)')
    top_20_key_skills_by_year_table = [
        d.split(': ') for d in top_20_key_skills_by_year_data.table_data.replace('\r\n', ' ').split(', ')
    ]
    skills_count = sum([int(d[1]) for d in top_20_key_skills_by_year_table])
    for d in top_20_key_skills_by_year_table:
        d[1] = str(round(int(d[1]) / skills_count, 3))
        if (len(d[1]) - d[1].find('.') - 1) < 3:
            d[1] += '0'
        percentage = round(float(d[1]) * 100, 2)
        d.append(f'{percentage}%')
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
    vacancy_name = VacancyDescription.objects.get(vacancy_name='Python-программист').vacancy_name

    # Динамика уровня зарплат по годам
    salary_by_year_data = VacancyStatistics.objects.get(name='Динамика уровня зарплат по годам (Python-программист)')
    salary_by_year_table = [d.split(': ') for d in salary_by_year_data.table_data.replace('\r\n', ' ').split(', ')]
    for d in salary_by_year_table:
        d[1] = '{0:,}'.format(float(d[1])).replace(',', ' ')
        if (len(d[1]) - d[1].find('.') - 1) < 2:
            d[1] += '0'

    # Динамика количества вакансий по годам
    vacancies_count_by_year_data = VacancyStatistics.objects.get(name='Динамика количества вакансий по годам (Python-программист)')
    vacancies_count_by_year_table = [d.split(': ') for d in vacancies_count_by_year_data.table_data.replace('\r\n', ' ').split(', ')]
    for d in vacancies_count_by_year_table:
        d[1] = '{0:,}'.format(int(d[1])).replace(',', ' ')

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

    # Уровень зарплат по городам (в порядке убывания)
    salary_by_area_data = VacancyStatistics.objects.get(name='Уровень зарплат по городам (Python-программист)')
    salary_by_area_table = [d.split(': ') for d in salary_by_area_data.table_data.replace('\r\n', ' ').split(', ')]
    for d in salary_by_area_table:
        d[1] = '{0:,}'.format(float(d[1])).replace(',', ' ')
        if (len(d[1]) - d[1].find('.') - 1) < 2:
            d[1] += '0'

    # Доля вакансий по городам
    vacancies_fraction_by_area_data = VacancyStatistics.objects.get(name='Доля вакансий по городам (Python-программист)')
    vacancies_fraction_by_area_table = [d.split(': ') for d in vacancies_fraction_by_area_data.table_data.replace('\r\n', ' ').split(', ')]
    for d in vacancies_fraction_by_area_table:
        if (len(d[1]) - d[1].find('.') - 1) < 3:
            d[1] += '0'
        percentage = round(float(d[1]) * 100, 2)
        d.append(f'{percentage}%')

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

    # Топ-20 навыков по годам
    top_20_key_skills_by_year_data = VacancyStatistics.objects.get(name='Топ-20 навыков по годам (Python-программист)')
    top_20_key_skills_by_year_table = [td.split(': ') for td in top_20_key_skills_by_year_data.table_data.replace('\r\n', ' ').split(', ')]
    skills_count = sum([int(d[1]) for d in top_20_key_skills_by_year_table])
    for d in top_20_key_skills_by_year_table:
        d[1] = str(round(int(d[1]) / skills_count, 3))
        if (len(d[1]) - d[1].find('.') - 1) < 3:
            d[1] += '0'
        percentage = round(float(d[1]) * 100, 2)
        d.append(f'{percentage}%')
    top_20_key_skills_by_year_table = sorted(top_20_key_skills_by_year_table, key=lambda x: x[1], reverse=True)

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
