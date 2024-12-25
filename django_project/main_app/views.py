from django.shortcuts import render
from .models import VacancyDescription


def index(request):
    content = VacancyDescription.objects.first()
    return render(request, 'index.html', {'content': content})


def general_statistics(request):
    return render(request, 'general-statistics.html')


def demand(request):
    return render(request, 'demand.html')


def geography(request):
    return render(request, 'geography.html')


def skills(request):
    return render(request, 'skills.html')


def latest_vacancies(request):
    return render(request, 'latest-vacancies.html')
