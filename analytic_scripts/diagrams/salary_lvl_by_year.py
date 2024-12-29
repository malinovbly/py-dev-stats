# Построение графика "Динамика уровня зарплат по годам" #
import matplotlib.pyplot as plt

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

fig, ax = plt.subplots()

ax.bar(salary_lvl_by_year.keys(),
       salary_lvl_by_year.values(),
       tick_label=salary_lvl_by_year.keys(),
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

# plt.savefig('C:/Users/Artemy/OneDrive/Рабочий стол/_Универ/ТП Python/salary_lvl_by_year.png', transparent=True)
plt.show()
