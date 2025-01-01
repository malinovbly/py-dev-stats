# Построение графика "Динамика количества вакансий по годам" #
import matplotlib.pyplot as plt


def create_vacs_cnt_by_year_diagram(data):
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

    # plt.savefig('vacs_cnt_by_year.png', transparent=True)
    # plt.savefig('vacancy_vacs_cnt_by_year.png', transparent=True)
    # plt.show()


if __name__ == '__main__':
    vacs_cnt_by_year = {
        2003: 1983,
        2004: 7833,
        2005: 16020,
        2006: 33321,
        2007: 53562,
        2008: 75070,
        2009: 52889,
        2010: 93494,
        2011: 142458,
        2012: 173896,
        2013: 234016,
        2014: 259569,
        2015: 284760,
        2016: 330064,
        2017: 385696,
        2018: 510632,
        2019: 529062,
        2020: 605772,
        2021: 935167,
        2022: 879505,
        2023: 704478,
        2024: 553443
    }
    create_vacs_cnt_by_year_diagram(vacs_cnt_by_year)

    vacancy_vacs_cnt_by_year = {
        2003: 0,
        2004: 0,
        2005: 0,
        2006: 5,
        2007: 10,
        2008: 38,
        2009: 60,
        2010: 169,
        2011: 389,
        2012: 714,
        2013: 1188,
        2014: 4263,
        2015: 4146,
        2016: 3039,
        2017: 3536,
        2018: 4840,
        2019: 5735,
        2020: 7689,
        2021: 13024,
        2022: 11696,
        2023: 10771,
        2024: 8491
    }
    create_vacs_cnt_by_year_diagram(vacancy_vacs_cnt_by_year)
