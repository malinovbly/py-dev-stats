import pandas as pd


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


if __name__ == '__main__':
    df_correct_vacs_only = pd.read_csv('vacancies_2024_correct_only.csv', sep=',', low_memory=False)

    salary_lvl_by_year_data = get_salary_lvl_by_year(df_correct_vacs_only)
    vacs_cnt_by_year_data = get_vacancies_count_by_year(df_correct_vacs_only)
    salary_lvl_by_area_data = get_salary_lvl_by_area(df_correct_vacs_only)
    vacs_frac_by_area_data = get_vacs_frac_by_area(df_correct_vacs_only)
