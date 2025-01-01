# Построение графика "Доля вакансий по городам (в порядке убывания)" #
import matplotlib.pyplot as plt


def create_vacs_frac_by_area_diagram(data):
    colors = [
        '#83b2c7',
        '#70AED0',
        '#78B7D9',
        '#88C9E5',
        '#90CFEA',
        '#68A5C8',
        '#70AFD1',
        '#7DB9D8',
        '#8DC8E1',
        '#76B5D5',
        '#8AC7E6',
        '#7ABFDE',
        '#86C4E1',
        '#79BDD9',
        '#81C7E3'
    ]

    fig, ax = plt.subplots()

    ax.pie(data.values(),
           labels=data.keys(),
           startangle=190,
           colors=colors,
           wedgeprops={
               "edgecolor" : "#a1b3be",
               'linewidth' : 0.2
           })
    plt.axis('equal')

    plt.tight_layout()

    # plt.savefig('vacs_frac_by_area.png', transparent=True)
    # plt.savefig('vacancy_vacs_frac_by_area.png', transparent=True)
    # plt.show()


if __name__ == '__main__':
    vacs_frac_by_area = {
        'Москва': 0.341,
        'Доля <1%': 0.333,
        'Санкт-Петербург': 0.102,
        'Минск': 0.03,
        'Новосибирск': 0.024,
        'Екатеринбург': 0.022,
        'Нижний Новгород': 0.021,
        'Алматы': 0.02,
        'Казань': 0.02,
        'Киев': 0.02,
        'Воронеж': 0.016,
        'Краснодар': 0.015,
        'Ростов-на-Дону': 0.013,
        'Самара': 0.013,
        'Пермь': 0.01
    }
    create_vacs_frac_by_area_diagram(vacs_frac_by_area)

    vacancy_vacs_frac_by_area = {
        'Москва': 0.379,
        'Доля <1%': 0.239,
        'Санкт-Петербург': 0.129,
        'Минск': 0.044,
        'Новосибирск': 0.029,
        'Екатеринбург': 0.026,
        'Казань': 0.026,
        'Нижний Новгород': 0.025,
        'Киев': 0.02,
        'Воронеж': 0.018,
        'Алматы': 0.015,
        'Ростов-на-Дону': 0.014,
        'Краснодар': 0.013,
        'Самара': 0.012,
        'Уфа': 0.01
    }
    create_vacs_frac_by_area_diagram(vacancy_vacs_frac_by_area)
