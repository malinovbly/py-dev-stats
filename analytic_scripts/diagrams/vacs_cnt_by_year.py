# Построение графика "Динамика количества вакансий по годам" #
import matplotlib.pyplot as plt

vacs_cnt_by_year = {
    2003: 1983,
    2004: 7833,
    2005: 16022,
    2006: 33321,
    2007: 53562,
    2008: 75070,
    2009: 52889,
    2010: 93494,
    2011: 142458,
    2012: 173897,
    2013: 234019,
    2014: 259571,
    2015: 284763,
    2016: 332460,
    2017: 391464,
    2018: 517670,
    2019: 535956,
    2020: 611885,
    2021: 943151,
    2022: 887542,
    2023: 709545,
    2024: 556742
}

fig, ax = plt.subplots()

ax.bar(vacs_cnt_by_year.keys(),
       vacs_cnt_by_year.values(),
       tick_label=vacs_cnt_by_year.keys(),
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

# plt.savefig('C:/Users/Artemy/OneDrive/Рабочий стол/_Универ/ТП Python/vacs_cnt_by_year.png', transparent=True)
plt.show()
