import file_operations
from faker import Faker
import random

FAKE = Faker("ru_RU")

SKILLS = [
    'Стремительный прыжок',
    'Электрический выстрел',
    'Стремительный удар',
    'Кислотный взгляд',
    'Тайный побег',
    'Ледяной выстрел',
    'Огненный заряд',
    'Ледяной удар',
]


LETTERS = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠',
    'Б': 'Б̋',
    'В': 'В͒͠',
    'Г': 'Г͒͠',
    'Д': 'Д̋',
    'Е': 'Е',
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒',
    'З': 'З̋̋͠',
    'И': 'И',
    'Й': 'Й͒͠',
    'К': 'К̋̋',
    'Л': 'Л̋͠',
    'М': 'М͒͠',
    'Н': 'Н͒',
    'О': 'О̋',
    'П': 'П̋͠',
    'Р': 'Р̋͠',
    'С': 'С͒',
    'Т': 'Т͒',
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠',
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠',
    'Ш': 'Ш͒͠',
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠',
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠',
    'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' '
}


RUNIC_SKILLS = []


def main():
    for h in SKILLS:
        if h in SKILLS:
            for i in LETTERS.keys():
                h = h.replace(i, LETTERS[i])
        RUNIC_SKILLS.append(h)
    for cards in range(10):
        skill = random.sample(RUNIC_SKILLS, 3)
        last_name = FAKE.last_name()
        first_name = FAKE.first_name()
        context = {
            "first_name": first_name,
            "last_name": last_name,
            "town": FAKE.city(),
            "job": FAKE.job(),
            'strength': random.randint(3, 18),
            'agility': random.randint(3, 18),
            'endurance': random.randint(3, 18),
            'intelligence': random.randint(3, 18),
            'luck': random.randint(3, 18),
            'skill_1': skill[0],
            'skill_2': skill[1],
            'skill_3': skill[2],
                    }
        name = ("cards/{} {}.svg").format(last_name, first_name)
        file_operations.render_template("charsheet.svg", name, context)


if __name__ == '__main__':
    main()
