import pandas as pd
from datetime import datetime
import requests
import bs4


## Возвращает список дат в формате dd/mm/YYYY (01/01/YYYY)
def get_all_dates(start_date, end_date):
    start_date = datetime.strptime(start_date, '%d/%m/%Y')
    end_date = datetime.strptime(end_date, '%d/%m/%Y')

    date_lst = []
    current_date = start_date
    while current_date <= end_date:
        date_lst.append(current_date.strftime('%d/%m/%Y'))
        if current_date.month == 12:
            current_date = current_date.replace(year=current_date.year + 1, month=1, day=1)
        else:
            current_date = current_date.replace(month=current_date.month + 1, day=1)

    return date_lst


## Возвращает df со всеми валютами за все время
def get_all_currencies():
    cb_api = 'https://www.cbr.ru/scripts/XML_daily.asp'
    first_date = '01/01/2003'
    last_date = '01/12/2024'
    date_lst = get_all_dates(first_date, last_date)

    all_currencies = list()
    for date in date_lst:
        data = requests.get(f'{cb_api}?date_req={date}')
        soup = bs4.BeautifulSoup(data.content, 'xml')
        valutes = soup.find_all('Valute')
        date_curs = dict()
        date_curs['date'] = f'{date[6:]}-{date[3:5]}'
        for v in valutes:
            code = v.find('CharCode').text
            value = float(v.find('VunitRate').text.replace(',', '.'))
            date_curs[code] = value
        all_currencies.append(date_curs)

    all_currencies_df = pd.DataFrame(all_currencies)
    return all_currencies_df


## Возвращает df с зарплатами, переведенными в рубли
def convert_salaries(df):
    all_currencies_df = get_all_currencies()

    coefs = list(
        1 if row[4] == 'RUR' or isinstance(row[4], float) or row[4] is None
        else float(all_currencies_df.loc[all_currencies_df['date'] == row[6][0:7], row[4]])
        for row in df.values
    )

    df = df.assign(coefs=coefs)
    df = (df
          .assign(converted_salary_from=df['salary_from'] * df['coefs'])
          .assign(converted_salary_to=df['salary_to'] * df['coefs'])
          .assign(converted_avg_salary=df['avg_salary'] * df['coefs'])
          )

    return df


## Удаление некорректных вакансий
def drop_incorrect_vacs(df):
    ## 1. С зарплатой > 10 000 000
    indexes = df[(df['converted_salary_from'] > 10000000) | (df['converted_salary_to'] > 10000000)].index
    df = df.drop(indexes)

    ## 2. С неизвестным курсом валюты
    indexes = df[(df['avg_salary'].notna()) & (df['coefs'].isna())].index
    df = df.drop(indexes)

    return df


## Фильтр по профессии
def filter_df_by_vac(df):
    filter_keywords = ['Python-программист', 'python', 'питон', 'пайтон']
    pattern = '|'.join(filter_keywords)
    result = df[df['name'].str.contains(pattern, case=False, na=False)]

    return result


if __name__ == '__main__':
    vacancies_2024_df = pd.read_csv('vacancies_2024.csv', sep=',', low_memory=False)
    df_copy = vacancies_2024_df.copy()
    df_copy = df_copy.assign(avg_salary=df_copy[['salary_from', 'salary_to']].astype(float).mean(axis=1))

    df_converted_salaries = convert_salaries(df_copy)
    df_correct_vacs_only = drop_incorrect_vacs(df_converted_salaries)
    df_correct_vacs_only.to_csv('vacancies_2024_correct_only.csv', index=False)

    df_filtered = filter_df_by_vac(df_correct_vacs_only)
    df_filtered.to_csv('filtered_vacancies.csv', index=False)
