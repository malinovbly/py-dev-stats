# Построение графика "Уровень зарплат по городам (в порядке убывания)" #
import matplotlib.pyplot as plt

salary_lvl_by_area = {
    'Москва': 98713.31,
    'Санкт-Петербург': 82815.67,
    'Новосибирск': 77665.64,
    'Минск': 76587.13,
    'Екатеринбург': 73017.63,
    'Казань': 66853.66,
    'Краснодар': 65404.44,
    'Нижний Новгород': 62999.02,
    'Самара': 61243.17,
    'Челябинск': 60995.54,
    'Уфа': 60737.05,
    'Красноярск': 60202.31,
    'Ростов-на-Дону': 57595.71,
    'Пермь': 56826.88,
    'Воронеж': 55189.37,
    'Алматы': 53967.41
}
salary_lvl_by_area = dict(sorted(salary_lvl_by_area.items(), key=lambda item: item[1], reverse=False))

fig, ax = plt.subplots()

ax.barh(salary_lvl_by_area.keys(),
       salary_lvl_by_area.values(),
       tick_label=salary_lvl_by_area.keys(),
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

# plt.savefig('C:/Users/Artemy/OneDrive/Рабочий стол/_Универ/ТП Python/salary_lvl_by_area.png', transparent=True)
plt.show()

