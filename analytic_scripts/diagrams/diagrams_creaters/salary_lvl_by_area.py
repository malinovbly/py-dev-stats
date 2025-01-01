# Построение графика "Уровень зарплат по городам (в порядке убывания)" #
import matplotlib.pyplot as plt


def create_salary_lvl_by_area_diagram(data):
    fig, ax = plt.subplots()

    ax.barh(data.keys(),
           data.values(),
           tick_label=data.keys(),
           edgecolor='black',
           linewidth=0.7,
           color='#83b2c7',
           zorder=3)

    ax.tick_params(axis='x')
    ax.tick_params(axis='y')
    plt.xticks(color='#4D4C49')
    plt.yticks(color='#4D4C49')

    ax.grid(axis='x', color='#4D4C49', zorder=0, alpha=0.5)

    ax.spines['top'].set_color('#4D4C49')
    ax.spines['bottom'].set_color('#4D4C49')
    ax.spines['left'].set_color('#4D4C49')
    ax.spines['right'].set_color('#4D4C49')

    plt.tight_layout()

    # plt.savefig('salary_lvl_by_area.png', transparent=True)
    # plt.savefig('vacancy_salary_lvl_by_area.png', transparent=True)
    # plt.show()


if __name__ == '__main__':
    salary_lvl_by_area = {
        'Москва': 98713.31,
        'Киев': 82948.06,
        'Санкт-Петербург': 82815.67,
        'Новосибирск': 77665.64,
        'Минск': 76587.13,
        'Екатеринбург': 73017.63,
        'Казань': 66853.66,
        'Краснодар': 65404.44,
        'Нижний Новгород': 62999.02,
        'Самара': 61243.17,
        'Ростов-на-Дону': 57595.71,
        'Пермь': 56826.88,
        'Воронеж': 55189.37,
        'Алматы': 53967.41
    }
    salary_lvl_by_area = dict(sorted(salary_lvl_by_area.items(), key=lambda item: item[1], reverse=False))
    create_salary_lvl_by_area_diagram(salary_lvl_by_area)

    vacancy_salary_lvl_by_area = {
        'Москва': 175513.42,
        'Минск': 161630.24,
        'Киев': 152350.13,
        'Казань': 147160.84,
        'Санкт-Петербург': 143730.24,
        'Самара': 143360.83,
        'Нижний Новгород': 142402.24,
        'Новосибирск': 140666.03,
        'Воронеж': 131387.84,
        'Екатеринбург': 127922.23,
        'Краснодар': 123515.42,
        'Ростов-на-Дону': 120732.61,
        'Алматы': 112150.53,
        'Уфа': 107261.07
    }
    vacancy_salary_lvl_by_area = dict(sorted(vacancy_salary_lvl_by_area.items(), key=lambda item: item[1], reverse=False))
    create_salary_lvl_by_area_diagram(vacancy_salary_lvl_by_area)
