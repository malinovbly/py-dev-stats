# Построение графика "Динамика уровня зарплат по годам" #
import matplotlib.pyplot as plt


def create_salary_lvl_by_year_diagram(data):
    fig, ax = plt.subplots()

    ax.bar(data.keys(),
           data.values(),
           tick_label=data.keys(),
           edgecolor='black',
           linewidth=0.7,
           color='#83b2c7',
           zorder=3)

    ax.tick_params(axis='x', rotation=90)
    ax.tick_params(axis='y')
    plt.xticks(color='#4D4C49')
    plt.yticks(color='#4D4C49')

    ax.grid(axis='y', color='#4D4C49', zorder=0, alpha=0.5)

    ax.spines['top'].set_color('#4D4C49')
    ax.spines['bottom'].set_color('#4D4C49')
    ax.spines['left'].set_color('#4D4C49')
    ax.spines['right'].set_color('#4D4C49')

    plt.tight_layout()

    # plt.savefig('salary_lvl_by_year.png', transparent=True)
    # plt.savefig('vacancy_salary_lvl_by_year.png', transparent=True)
    # plt.show()


if __name__ == '__main__':
    salary_lvl_by_year = {
        2003: 1366.92,
        2004: 1488.88,
        2005: 1584.67,
        2006: 1522.75,
        2007: 5604.62,
        2008: 27478.63,
        2009: 37548.84,
        2010: 40958.99,
        2011: 42359.96,
        2012: 44525.21,
        2013: 46082.5,
        2014: 47957.63,
        2015: 50649.73,
        2016: 55206.32,
        2017: 63492.74,
        2018: 67200.09,
        2019: 80231.72,
        2020: 93384.36,
        2021: 109520.0,
        2022: 133568.71,
        2023: 175731.04,
        2024: 201185.41
    }
    create_salary_lvl_by_year_diagram(salary_lvl_by_year)

    vacancy_salary_lvl_by_year = {
        2003: 0,
        2004: 0,
        2005: 0,
        2006: 920.0,
        2007: 2218.75,
        2008: 25987.5,
        2009: 51182.22,
        2010: 47706.25,
        2011: 46307.35,
        2012: 60077.02,
        2013: 56032.0,
        2014: 66362.21,
        2015: 69586.84,
        2016: 89384.28,
        2017: 99273.62,
        2018: 101811.34,
        2019: 113526.01,
        2020: 125585.99,
        2021: 159374.69,
        2022: 228441.87,
        2023: 259172.98,
        2024: 395375.09
    }
    create_salary_lvl_by_year_diagram(vacancy_salary_lvl_by_year)
