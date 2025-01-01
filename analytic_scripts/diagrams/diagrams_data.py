import pandas as pd
from collections import Counter


## Динамика уровня зарплат по годам
def get_salary_lvl_by_year(vacancies):
    years = list(i for i in range(2003, 2024 + 1))
    vc_copy = vacancies.copy()
    year_groups = vc_copy.groupby(vc_copy.published_at.str[:4])

    salary_lvl_by_year = dict()
    for year in years:
            key = str(year)
            if key in year_groups.groups:
                group = year_groups.get_group(key)
                salary = round(float(group['avg_salary'].mean(axis=0)), 2)
                salary_lvl_by_year[year] = salary
            else:
                salary_lvl_by_year[year] = 0

    return salary_lvl_by_year


## Динамика количества вакансий по годам
def get_vacancies_count_by_year(vacancies):
    years = list(i for i in range(2003, 2024 + 1))
    vc_copy = vacancies.copy()
    year_groups = vc_copy.groupby(vc_copy.published_at.str[:4])

    vacs_cnt_by_year = dict()
    for year in years:
        key = str(year)
        if key in year_groups.groups:
            item = year_groups.get_group(key)
            vacs_count = len(item)
            vacs_cnt_by_year[year] = vacs_count
        else:
            vacs_cnt_by_year[year] = 0

    return vacs_cnt_by_year


## Динамика уровня зарплат по городам (в порядке убывания)
def get_salary_lvl_by_area(vacancies):
    vc_copy = vacancies.copy()
    area_groups = (vc_copy
                   .groupby(vc_copy['area_name'])
                   .filter(lambda x: (len(x) / len(vc_copy) * 100) >= 1)
                   .groupby('area_name')
                   )
    areas = set(vc_copy['area_name'])

    salary_lvl_by_area = dict()
    for area in areas:
            key = str(area)
            if key in area_groups.groups:
                group = area_groups.get_group(key)
                salary = round(float(group['converted_avg_salary'].mean(axis=0)), 2)
                salary_lvl_by_area[area] = salary
            else:
                salary_lvl_by_area[area] = 0

    return salary_lvl_by_area


## Доля вакансий по городам (в порядке убывания)
def get_vacs_frac_by_area(vacancies):
    vc_copy = vacancies.copy()
    area_groups = (vc_copy
                   .groupby(vc_copy['area_name'])
                   .filter(lambda x: (len(x) / len(vc_copy) * 100) >= 1)
                   .groupby('area_name')
                   )

    vacs_frac_by_area = dict()
    for key in area_groups.groups:
        group = area_groups.get_group(key)
        vacs_frac_by_area[key] = round(len(group) / len(vc_copy), 3)

    return vacs_frac_by_area


## Топ-20 навыков по годам.
def get_top_20_key_skills_by_year(vacancies):

    ## 20 самых популярных навыков
    def get_top_20_key_skills(vacancies):
        key_skills = (vacancies['key_skills']
                      .dropna()
                      .str.split('\n')
                      .explode()
                      .tolist()
                      )
        c = Counter(key_skills)
        return c.most_common(20)

    top_20_key_skills = dict(get_top_20_key_skills(vacancies))

    vc_copy = vacancies.copy()
    year_groups = vc_copy.groupby(vc_copy.published_at.str[:4])

    skills_by_year = dict()
    for year in year_groups.groups.keys():
        group = year_groups.get_group(str(year))['key_skills'].dropna().str.split('\n').explode().tolist()
        counter = Counter(group)

        year_dynamic = list()
        for key, value in counter.items():
            if key in top_20_key_skills.keys():
                year_dynamic.append((key, value))
        year_dynamic = sorted(year_dynamic, key=lambda x: x[0])

        skills_by_year[int(year)] = year_dynamic

    return skills_by_year


if __name__ == '__main__':
    ## Все вакансии (корректные)
    correct_vacs = pd.read_csv('vacancies_2024_correct_only.csv', sep=',', low_memory=False)

    salary_lvl_by_year_data = get_salary_lvl_by_year(correct_vacs)
    vacs_cnt_by_year_data = get_vacancies_count_by_year(correct_vacs)
    salary_lvl_by_area_data = get_salary_lvl_by_area(correct_vacs)
    vacs_frac_by_area_data = get_vacs_frac_by_area(correct_vacs)
    top_20_key_skills_by_year = get_top_20_key_skills_by_year(correct_vacs)


    ## Вакансии, отфильтрованные по профессии 'Python-программист'
    filtered_vacs = pd.read_csv('filtered_vacancies.csv', sep=',', low_memory=False)

    vacancy_salary_lvl_by_year_data = get_salary_lvl_by_year(filtered_vacs)
    vacancy_vacs_cnt_by_year_data = get_vacancies_count_by_year(filtered_vacs)
    vacancy_salary_lvl_by_area_data = get_salary_lvl_by_area(filtered_vacs)
    vacancy_vacs_frac_by_area_data = get_vacs_frac_by_area(filtered_vacs)
    vacancy_top_20_key_skills_by_year = get_top_20_key_skills_by_year(filtered_vacs)
