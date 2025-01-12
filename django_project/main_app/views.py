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
    return render(
        request,
        'general-statistics.html',
        {
            'salary_by_year': get_stats('Динамика уровня зарплат по годам'),
            'vacancies_count_by_year': get_stats('Динамика количества вакансий по годам'),
            'salary_by_area': get_stats('Уровень зарплат по городам'),
            'vacancies_fraction_by_area': get_stats('Доля вакансий по городам'),
            'top_20_key_skills_by_year': get_stats('Топ-20 навыков по годам')
        }
    )


def demand(request):
    vacancy_name = VacancyDescription.objects.get(vacancy_name='Python-программист').vacancy_name
    return render(
        request,
        'demand.html',
        {
            'vacancy_name': vacancy_name,
            'salary_by_year': get_stats('Динамика уровня зарплат по годам', vacancy_name),
            'vacancies_count_by_year': get_stats('Динамика количества вакансий по годам', vacancy_name)
        }
    )


def geography(request):
    vacancy_name = VacancyDescription.objects.get(vacancy_name='Python-программист').vacancy_name
    return render(
        request,
        'geography.html',
        {
            'vacancy_name': vacancy_name,
            'salary_by_area': get_stats('Уровень зарплат по городам', vacancy_name),
            'vacancies_fraction_by_area': get_stats('Доля вакансий по городам', vacancy_name)
        }
    )


def skills(request):
    vacancy_name = VacancyDescription.objects.get(vacancy_name='Python-программист').vacancy_name
    return render(
        request,
        'skills.html',
        {
            'vacancy_name': vacancy_name,
            'top_20_key_skills_by_year': get_stats('Топ-20 навыков по годам', vacancy_name)
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
    return VacancyStatistics.objects.get(name=f'{data_name} ({vacancy_name})')


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
