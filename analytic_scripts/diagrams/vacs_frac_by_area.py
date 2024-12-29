# Построение графика "Доля вакансий по городам (в порядке убывания)" #
import matplotlib.pyplot as plt

vacs_frac_by_area = {
    'Города с долей <1%': 0.385,
    'Москва': 0.28,
    'Санкт-Петербург': 0.103,
    'Новосибирск': 0.025,
    'Екатеринбург': 0.024,
    'Казань': 0.022,
    'Нижний Новгород': 0.021,
    'Алматы': 0.018,
    'Краснодар': 0.018,
    'Ростов-на-Дону': 0.017,
    'Воронеж': 0.015,
    'Самара': 0.014,
    'Минск': 0.012,
    'Пермь': 0.012,
    'Красноярск': 0.011,
    'Уфа': 0.011,
    'Челябинск': 0.011,
}

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
    '#81C7E3',
    '#99D2EB',
    '#B3DCF5'
]

fig, ax = plt.subplots()

ax.pie(vacs_frac_by_area.values(),
       labels=vacs_frac_by_area.keys(),
       startangle=210,
       colors=colors,
       wedgeprops={
           "edgecolor" : "#a1b3be",
           'linewidth' : 0.2
       })
plt.axis('equal')

plt.tight_layout()

plt.savefig('C:/Users/Artemy/OneDrive/Рабочий стол/_Универ/ТП Python/vacs_frac_by_area.png', transparent=True)
# plt.show()
