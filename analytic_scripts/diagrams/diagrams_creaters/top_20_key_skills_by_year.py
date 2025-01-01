# Построение графика "Топ-20 навыков по годам" #
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def create_top_20_key_skills_by_year_diagram(skills_by_year, top_skills):
    colors = [
        '#8cbdd9',
        '#7eb4d8',
        '#70abd7',
        '#62a3d6',
        '#549bd5',
        '#4793d4',
        '#398bd3',
        '#2c83d2',
        '#1f7bd1',
        '#1274d0',
        '#056dcc',
        '#0065bb',
        '#005daa',
        '#00549a',
        '#004b8b',
        '#00427b',
        '#00396b',
        '#00305c',
        '#00284d',
        '#001f3e',
    ]

    years = list(skills_by_year.keys())
    labels = list(top_skills.keys())
    data = {label: [0] * len(years) for label in labels}

    for year_index, year in enumerate(years):
        for skill, count in top_20_key_skills_by_year[year]:
            if skill in data:
                data[skill][year_index] = count

    fig, ax = plt.subplots()

    bottom_values = [0] * len(years)
    for skill_index, skill in enumerate(labels):
        ax.bar(years,
               data[skill],
               bottom=bottom_values,
               label=skill,
               color=colors[skill_index],
               zorder=3)
        bottom_values = [bottom + value for bottom, value in zip(bottom_values, data[skill])]

    ax.legend(title='Навыки', bbox_to_anchor=(1, 1.05), facecolor='#a1b3be').get_frame().set_edgecolor('#a1b3be')

    ax.tick_params(axis='x', rotation=90)
    ax.tick_params(axis='y')
    plt.xticks(years, color='#4D4C49')
    plt.yticks(color='#4D4C49')

    ax.grid(axis='y', color='#4D4C49', zorder=0, alpha=0.5)

    ax.spines['top'].set_color('#4D4C49')
    ax.spines['bottom'].set_color('#4D4C49')
    ax.spines['left'].set_color('#4D4C49')
    ax.spines['right'].set_color('#4D4C49')

    formatter = ticker.StrMethodFormatter("{x:.0f}")
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.tight_layout()

    # plt.savefig('top_20_key_skills_by_year.png', transparent=True)
    # plt.savefig('vacancy_top_20_key_skills_by_year.png', transparent=True)
    # plt.show()



if __name__ == '__main__':
    top_20_key_skills = {
        '1С программирование': 126551,
        'Adobe Photoshop': 146677,
        'CSS': 158343,
        'Git': 315573,
        'HTML': 185399,
        'Java': 190147,
        'JavaScript': 284717,
        'Linux': 267272,
        'MySQL': 154633,
        'PHP': 161510,
        'PostgreSQL': 175411,
        'Python': 221022,
        'SQL': 412684,
        'Английский язык': 284726,
        'Ведение переговоров': 140441,
        'Грамотная речь': 240143,
        'ООП': 129336,
        'Пользователь ПК': 235416,
        'Работа в команде': 333190,
        'Управление проектами': 208048
    }
    top_20_key_skills = dict(sorted(top_20_key_skills.items(), key=lambda item: item[1], reverse=True))
    top_20_key_skills_by_year = {
        # 2003: [], 2004: [], 2005: [], 2006: [], 2007: [], 2008: [],
        # 2009: [], 2010: [], 2011: [], 2012: [], 2013: [], 2014: [],
        2015: [('1С программирование', 657), ('Adobe Photoshop', 1274), ('CSS', 3015), ('Git', 2528), ('HTML', 3791),
               ('Java', 2312), ('JavaScript', 6702), ('Linux', 1683), ('MySQL', 2430), ('PHP', 2765),
               ('PostgreSQL', 652), ('Python', 787), ('SQL', 2148), ('Английский язык', 1732),
               ('Ведение переговоров', 2434), ('Грамотная речь', 1284), ('ООП', 5146), ('Пользователь ПК', 1496),
               ('Работа в команде', 1563), ('Управление проектами', 1977)],
        2016: [('1С программирование', 2585), ('Adobe Photoshop', 4024), ('CSS', 8045), ('Git', 8413), ('HTML', 9674),
               ('Java', 6410), ('JavaScript', 13387), ('Linux', 4978), ('MySQL', 7538), ('PHP', 8903),
               ('PostgreSQL', 2959), ('Python', 3225), ('SQL', 6537), ('Английский язык', 4907),
               ('Ведение переговоров', 8284), ('Грамотная речь', 5415), ('ООП', 5989), ('Пользователь ПК', 6629),
               ('Работа в команде', 7023), ('Управление проектами', 6289)],
        2017: [('1С программирование', 4105), ('Adobe Photoshop', 4961), ('CSS', 12411), ('Git', 12433),
               ('HTML', 14153), ('Java', 8364), ('JavaScript', 19881), ('Linux', 7893), ('MySQL', 10994),
               ('PHP', 12465), ('PostgreSQL', 4688), ('Python', 4698), ('SQL', 9863), ('Английский язык', 6736),
               ('Ведение переговоров', 9872), ('Грамотная речь', 6036), ('ООП', 7809), ('Пользователь ПК', 6939),
               ('Работа в команде', 7905), ('Управление проектами', 8561)],
        2018: [('1С программирование', 6437), ('Adobe Photoshop', 6866), ('CSS', 17252), ('Git', 19295),
               ('HTML', 19720), ('Java', 12872), ('JavaScript', 27704), ('Linux', 12341), ('MySQL', 15406),
               ('PHP', 16788), ('PostgreSQL', 7447), ('Python', 9201), ('SQL', 16010), ('Английский язык', 10716),
               ('Ведение переговоров', 14845), ('Грамотная речь', 9551), ('ООП', 9699), ('Пользователь ПК', 11182),
               ('Работа в команде', 12859), ('Управление проектами', 13392)],
        2019: [('1С программирование', 9432), ('Adobe Photoshop', 8450), ('CSS', 19229), ('Git', 24955),
               ('HTML', 21670), ('Java', 17055), ('JavaScript', 31273), ('Linux', 18047), ('MySQL', 15863),
               ('PHP', 17106), ('PostgreSQL', 10643), ('Python', 14684), ('SQL', 25498), ('Английский язык', 19402),
               ('Ведение переговоров', 17647), ('Грамотная речь', 15458), ('ООП', 11452), ('Пользователь ПК', 18123),
               ('Работа в команде', 19597), ('Управление проектами', 17702)],
        2020: [('1С программирование', 15686), ('Adobe Photoshop', 15066), ('CSS', 25099), ('Git', 45296),
               ('HTML', 27599), ('Java', 30631), ('JavaScript', 40976), ('Linux', 36429), ('MySQL', 22201),
               ('PHP', 20612), ('PostgreSQL', 21896), ('Python', 28013), ('SQL', 56575), ('Английский язык', 43068),
               ('Ведение переговоров', 20693), ('Грамотная речь', 33220), ('ООП', 17671), ('Пользователь ПК', 36784),
               ('Работа в команде', 38462), ('Управление проектами', 27509)],
        2021: [('1С программирование', 24171), ('Adobe Photoshop', 32923), ('CSS', 32513), ('Git', 74031),
               ('HTML', 37462), ('Java', 42702), ('JavaScript', 58216), ('Linux', 57781), ('MySQL', 30116),
               ('PHP', 28846), ('PostgreSQL', 36084), ('Python', 49823), ('SQL', 96185), ('Английский язык', 85828),
               ('Ведение переговоров', 35023), ('Грамотная речь', 76179), ('ООП', 27477), ('Пользователь ПК', 61025),
               ('Работа в команде', 95348), ('Управление проектами', 50914)],
        2022: [('1С программирование', 27084), ('Adobe Photoshop', 34498), ('CSS', 21657), ('Git', 67528),
               ('HTML', 26420), ('Java', 33982), ('JavaScript', 45345), ('Linux', 57725), ('MySQL', 24723),
               ('PHP', 25451), ('PostgreSQL', 37184), ('Python', 47729), ('SQL', 89635), ('Английский язык', 70324),
               ('Ведение переговоров', 16623), ('Грамотная речь', 47223), ('ООП', 25110), ('Пользователь ПК', 51962),
               ('Работа в команде', 91094), ('Управление проектами', 44946)],
        2023: [('1С программирование', 21976), ('Adobe Photoshop', 23906), ('CSS', 12317), ('Git', 37580),
               ('HTML', 15196), ('Java', 20697), ('JavaScript', 25128), ('Linux', 40894), ('MySQL', 15778),
               ('PHP', 17885), ('PostgreSQL', 30366), ('Python', 35624), ('SQL', 62205), ('Английский язык', 26908),
               ('Ведение переговоров', 10723), ('Грамотная речь', 31559), ('ООП', 12654), ('Пользователь ПК', 27880),
               ('Работа в команде', 44825), ('Управление проектами', 26342)],
        2024: [('1С программирование', 14418), ('Adobe Photoshop', 14709), ('CSS', 6805), ('Git', 23514),
               ('HTML', 9714), ('Java', 15122), ('JavaScript', 16105), ('Linux', 29501), ('MySQL', 9584),
               ('PHP', 10689), ('PostgreSQL', 23492), ('Python', 27238), ('SQL', 48028), ('Английский язык', 15105),
               ('Ведение переговоров', 4297), ('Грамотная речь', 14218), ('ООП', 6329), ('Пользователь ПК', 13396),
               ('Работа в команде', 14514), ('Управление проектами', 10416)]
    }
    create_top_20_key_skills_by_year_diagram(top_20_key_skills_by_year, top_20_key_skills)

    vacancy_top_20_key_skills = {
        'Python': 51633,
        'PostgreSQL': 19297,
        'Git': 18586,
        'Django Framework': 17857,
        'SQL': 15384,
        'Linux': 15012,
        'Docker': 7871,
        'JavaScript': 5970,
        'Flask': 5505,
        'MySQL': 4886,
        'Redis': 4862,
        'Английский язык': 4455,
        'ООП': 4254,
        'MongoDB': 3832,
        'RabbitMQ': 3393,
        'Django': 3296,
        'REST': 3021,
        'HTML': 2588,
        'C++': 2302,
        'CSS': 2287
    }
    vacancy_top_20_key_skills = dict(sorted(vacancy_top_20_key_skills.items(), key=lambda item: item[1], reverse=True))
    vacancy_top_20_key_skills_by_year = {
        # '2006': [], '2007': [], '2008': [], '2009': [], '2010': [],
        # '2011': [], '2012': [], '2013': [], '2014': [],
        2015: [('C++', 20), ('CSS', 32), ('Django', 87), ('Django Framework', 168), ('Docker', 3), ('Flask', 26),
                 ('Git', 86), ('HTML', 33), ('JavaScript', 60), ('Linux', 104), ('MongoDB', 29), ('MySQL', 72),
                 ('PostgreSQL', 104), ('Python', 324), ('REST', 6), ('RabbitMQ', 85), ('Redis', 20), ('SQL', 55),
                 ('Английский язык', 10), ('ООП', 33)],
        2016: [('C++', 118), ('CSS', 124), ('Django', 39), ('Django Framework', 588), ('Docker', 37), ('Flask', 85),
                 ('Git', 313), ('HTML', 110), ('JavaScript', 340), ('Linux', 405), ('MongoDB', 114), ('MySQL', 185),
                 ('PostgreSQL', 366), ('Python', 1281), ('REST', 62), ('RabbitMQ', 103), ('Redis', 69), ('SQL', 275),
                 ('Английский язык', 25), ('ООП', 136)],
        2017: [('C++', 124), ('CSS', 146), ('Django', 17), ('Django Framework', 732), ('Docker', 74), ('Flask', 133),
                 ('Git', 531), ('HTML', 168), ('JavaScript', 434), ('Linux', 543), ('MongoDB', 151), ('MySQL', 244),
                 ('PostgreSQL', 534), ('Python', 1674), ('REST', 100), ('RabbitMQ', 75), ('Redis', 122), ('SQL', 272),
                 ('Английский язык', 82), ('ООП', 153)],
        2018: [('C++', 197), ('CSS', 253), ('Django', 32), ('Django Framework', 1207), ('Docker', 159),
                 ('Flask', 305), ('Git', 817), ('HTML', 275), ('JavaScript', 615), ('Linux', 721), ('MongoDB', 233),
                 ('MySQL', 394), ('PostgreSQL', 935), ('Python', 2734), ('REST', 192), ('RabbitMQ', 139),
                 ('Redis', 249), ('SQL', 585), ('Английский язык', 96), ('ООП', 209)],
        2019: [('C++', 207), ('CSS', 277), ('Django', 63), ('Django Framework', 1580), ('Docker', 302),
                 ('Flask', 374), ('Git', 1141), ('HTML', 282), ('JavaScript', 667), ('Linux', 1018), ('MongoDB', 369),
                 ('MySQL', 513), ('PostgreSQL', 1359), ('Python', 3752), ('REST', 193), ('RabbitMQ', 242),
                 ('Redis', 369), ('SQL', 809), ('Английский язык', 195), ('ООП', 295)],
        2020: [('C++', 460), ('CSS', 354), ('Django', 82), ('Django Framework', 2437), ('Docker', 430),
                 ('Flask', 532), ('Git', 2305), ('HTML', 389), ('JavaScript', 965), ('Linux', 1954), ('MongoDB', 553),
                 ('MySQL', 771), ('PostgreSQL', 2375), ('Python', 6151), ('REST', 295), ('RabbitMQ', 217),
                 ('Redis', 544), ('SQL', 1709), ('Английский язык', 569), ('ООП', 593)],
        2021: [('C++', 493), ('CSS', 443), ('Django', 470), ('Django Framework', 4382), ('Docker', 1299),
                 ('Flask', 1210), ('Git', 4795), ('HTML', 503), ('JavaScript', 1194), ('Linux', 3433), ('MongoDB', 820),
                 ('MySQL', 1059), ('PostgreSQL', 3835), ('Python', 11143), ('REST', 567), ('RabbitMQ', 539),
                 ('Redis', 1018), ('SQL', 3746), ('Английский язык', 1316), ('ООП', 1026)],
        2022: [('C++', 330), ('CSS', 397), ('Django', 834), ('Django Framework', 3450), ('Docker', 2083),
                 ('Flask', 1268), ('Git', 4433), ('HTML', 411), ('JavaScript', 805), ('Linux', 3400), ('MongoDB', 679),
                 ('MySQL', 795), ('PostgreSQL', 4276), ('Python', 10420), ('REST', 512), ('RabbitMQ', 730),
                 ('Redis', 796), ('SQL', 3618), ('Английский язык', 1407), ('ООП', 884)],
        2023: [('C++', 222), ('CSS', 177), ('Django', 1135), ('Django Framework', 2113), ('Docker', 2050),
                 ('Flask', 981), ('Git', 2667), ('HTML', 260), ('JavaScript', 467), ('Linux', 2126), ('MongoDB', 485),
                 ('MySQL', 550), ('PostgreSQL', 3271), ('Python', 8221), ('REST', 594), ('RabbitMQ', 760),
                 ('Redis', 921), ('SQL', 2619), ('Английский язык', 531), ('ООП', 623)],
        2024: [('C++', 131), ('CSS', 84), ('Django', 537), ('Django Framework', 1200), ('Docker', 1434),
                 ('Flask', 591), ('Git', 1498), ('HTML', 157), ('JavaScript', 423), ('Linux', 1308), ('MongoDB', 399),
                 ('MySQL', 303), ('PostgreSQL', 2242), ('Python', 5933), ('REST', 500), ('RabbitMQ', 503),
                 ('Redis', 754), ('SQL', 1696), ('Английский язык', 224), ('ООП', 302)]}
    create_top_20_key_skills_by_year_diagram(vacancy_top_20_key_skills_by_year, vacancy_top_20_key_skills)
