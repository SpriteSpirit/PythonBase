"""raw_list = ["сельдь-черноспинка", "морская камбала", "тунец", "ставрида", "морской окунь", "треска", "сайра",
            "морская камбала", "ставрида", "треска", "треска", "треска", "тунец", "ставрида", "морская камбала",
            "тунец", "морская камбала", "морская камбала", "морская камбала", "морская камбала", "тунец",
            ]
unique_list = []
temp = [unique_list.append(fish) for fish in raw_list if fish not in unique_list]
total = len(unique_list)

print(f"Всего {total} видов рыб")
print("\n".join(fish for fish in sorted(unique_list)))

fruits = ["orange", "apple", "banana"]
fruits.insert(1, "grape")
fruits.sort(reverse=False)
fruits = [fruit.title() for fruit in fruits]

print(fruits)


fruits = [{"name": "Apple", "price": 10, "available": 8},
          {"name": "Banana", "price": 13, "available": 2},
          {"name": "Grape", "price": 9, "available": 6}]

fruits[0]["apples"] = 15
fruits[1]["peach"] = 11

# print(fruits)
# print(fruits[0])

temp = [fruit for fruit in fruits if fruit["available"] > 5]
print(temp)

for fruit in fruits:
    fruit["price"] /= 2
print(fruits)

employees = {}
data = []
key_words = ["f", "i", "o", "pass", "birthday", "phone", "position"]

with open("person_date.txt", 'rt', encoding="utf-8") as data_file:
    for info in data_file:
        info = info.replace("#", "").strip()
        one_part = info.split(" / ")
        data.append(one_part)
# print(data)

for user in data:
    employees[user[0]] = employees.get(user[0], {})
    for index, i_data in enumerate(key_words):
        employees[user[0]][i_data] = user[index]

# print(employees)


for employee in employees.values():
    for key, value in employee.items():
        print(key, value)
    print("-")
#####################################################
employees = {
    "Киселёв": {"f": "Киселёв", "i": "Всеволод", "o": "Эдуардович", "pass": "342 020",
                "birthday": "14 ноября 2001 года",
                "phone": "+7 (908) 161-64-28", "position": "главный инженер"},
    "Довлатова": {"f": "Довлатова", "i": "Эмилия", "o": "Ефимовна", "pass": "342 000",
                  "birthday": "18 мая 2001 года",
                  "phone": "+7 (924) 588-50-15", "position": "технолог"},
    "Аверин": {"f": "Аверин", "i": "Мартын", "o": "Егорович", "pass": "217 340",
               "birthday": "12 февраля 1981 года",
               "phone": "+7 (933) 768-22-15", "position": "технолог"},
    "Князева": {"f": "Князева", "i": "Августа", "o": "Егоровна", "pass": "320 021",
                "birthday": "2 июля 1984 года",
                "phone": "+7 (965) 886-27-01", "position": "расфасовщик"},
    "Шанская": {"f": "Шанская", "i": "Аграфена", "o": "Семёновна", "pass": "116 404",
                "birthday": "7 июля 1982 года",
                "phone": "+7 (954) 940-47-96", "position": "психолог для рыб"},
}

for employee in employees.values():
    for key, value in employee.items():
        print(key, value)
    print("-")


# С рыбками хорошо работать — они ведут себя тихо и не кусаются. Главное — работникам не заболеть!
# Перенесите в подсписок vaccinated только сотрудников, которые прошли вакцинацию, а остальных отправьте
# в not_vaccinated. Затем распечатайте оба списка в таком формате:

# Вакцинированные:
# Киселёв Всеволод Эдуардович
# ...
# Остальные:
# Довлатова Эмилия Ефимовна


employees = [
    {"fio": "Киселёв Всеволод Эдуардович", "vaccinated": True},
    {"fio": "Довлатова Эмилия Ефимовна", "vaccinated": False},
    {"fio": "Аверин Мартын Егорович", "vaccinated": True},
    {"fio": "Князева Августа Егоровна", "vaccinated": False},
    {"fio": "Шанская Аграфена Семёновна", "vaccinated": True},
    {"fio": "Куприна Марина Викторовна", "vaccinated": False},
    {"fio": "Селезнёв Константин Игоревич", "vaccinated": False},
]

vaccinated = []
not_vaccinated = []

for employee in employees:
    for k, v in employee.items():
        if k == "vaccinated" and v:
            vaccinated.append(employee)
        elif k == "vaccinated" and not v:
            not_vaccinated.append(employee)

print('Вакцинированные:')
print('\n'.join([employee["fio"] for employee in vaccinated]))
print('Остальные:')
print('\n'.join([employee["fio"] for employee in not_vaccinated]))


# Некоторые рыбы предпочитают морскую воду, некоторые — пресную. Разделите список словарей на два, затем выведите
# названия вида из каждого словаря в строку. Вот так:

# Морские: Тунец, Скумбрия
# Пресноводные: Красноперка, Карась

fish = [
    {"specie": "Белуга", "water": "fresh"},
    {"specie": "Карась", "water": "fresh"},
    {"specie": "Красноперка", "water": "fresh"},
    {"specie": "Морской окунь", "water": "sea"},
    {"specie": "Тунец", "water": "sea"},
    {"specie": "Скумбрия", "water": "sea"}
]

sea_water = []
fresh_water = []

for each in fish:
    for k, v in each.items():
        if k == "water":
            if v == "fresh":
                fresh_water.append(each)
            else:
                sea_water.append(each)

print("Морские:", end=" ")
print(", ".join([fish["specie"] for fish in sea_water]))
print("Пресноводные:", end=" ")
print(", ".join([fish["specie"] for fish in fresh_water]))


# В словаре хранится информация о некоторых рыбах.
# Когда пользователь вводит с клавиатуры название рыбы, программа должна вывести информацию о ней.
# Если такой рыбы в словаре нет, появляется текст «Информация не найдена».
# Формат вывода:
# Лещ: Единственный представитель рода лещей из семейства карповых.
# Пресноводная рыба
# Промысловый размер: 29 см
#
# Формат вывода:
# Информация не найдена

species = [
    {"specie": "Лещ", "len": "29", "sea": False,
     "desc": "Единственный представитель рода лещей из семейства карповых."},
    {"specie": "Щука", "len": "45", "sea": False, "desc": "Распространена в пресных водах Евразии и Северной Америки. "
                                                          "Живет обычно в прибрежной зоне, в водных зарослях, "
                                                          "в непроточных или слабопроточных водах. "},
    {"specie": "Треска", "len": "33", "sea": True,
     "desc": "Треска встречается от прибрежной полосы до континентального "
             "шельфа, но в открытом море над большими глубинами редко. Ее "
             "жизненный цикл привязан к морским течениям Северной Атлантики."},
    {"specie": "Камбала", "len": "25", "sea": True,
     "desc": "Тело плоское, сильно сжато с боков, глаза расположены не по "
             "бокам головы, а смещены на одну ее сторону. Плавательного "
             "пузыря нет. "},
    {"specie": "Лосось", "len": "50", "sea": False, "desc": "Проходная форма обитает в северной части Атлантического "
                                                            "океана. Заходит на нерест в реки от Португалии и Испании "
                                                            "до Баренцева моря."},
]

s = input("s: ")

for fish in species:
    if s.lower() == fish['specie'].lower():
        print(f"{fish['specie']}: {fish['desc']}")
        print("Пресноводная рыба" if not fish['sea'] else "Морская рыба")
        print(f"Промысловый размер: {fish['len']} см")
        break
else:
    print("Информация не найдена")


# Одна из типичных задач при работе с данными — перекладывание их из одного формата в другой.
# Мы хотим отправить несколько контейнеров с живой рыбой в соседний питомник, но чтобы занести во внутреннюю
# систему задачу от внешнего заказчика, нужно перевести заказ из «их формата» в «наш формат».
#
# Формат заказчика:
# {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300}
# Наш формат:
# {"count": 5, "specie": "Тунец" , "avg_size": 30 }

# Заказчик называет ключи транслитом, хранит количество рыб в типе с точкой, размер рыбы в миллиметрах, а породу пишет
# с маленькой буквы. Просто катастрофа, а не заказчик! Придется писать конвертер.

order = [
    {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
    {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
    {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = []

for fish in order:
    order_converted.append(
        {"count": int(fish["skolko"]), "specie": fish["poroda"].title(), "avg_size": fish["sred_razmer"] // 10})

# Не удаляйте текст ниже, он нужен для проверки

for item in order_converted:
    for key, value in item.items():
        print(key, value)


# В списке хранится информация о прудах, где живут рыбы. Удалите из списка все пруды,где живут тунцы.

ponds = [
    {"pk": 1, "volume": 10000, "fish": "тунец"},
    {"pk": 192, "volume": 20000, "fish": "морская камбала"},
    {"pk": 206, "volume": 10000, "fish": "треска"},
    {"pk": 322, "volume": 25000, "fish": "тунец"},
    {"pk": 420, "volume": 20000, "fish": "морская камбала"},
    {"pk": 704, "volume": 10000, "fish": "треска"},
    {"pk": 920, "volume": 25000, "fish": "тунец"},
]

for pond in ponds:
    if pond['fish'] == "тунец":
        ponds.remove(pond)

# Не удаляйте код ниже, это код проверки

for pond in ponds:
    print(pond["pk"])
"""

# Поиск по спискам — не самая удобная операция, если значения хранятся внутри словарей. Давайте напишем функцию,
# которая выполняет поиск. Обратите внимание, функция должна возвращать два значения: название рыбы и воду,
# в которой она живет. Используйте кортеж для этой цели.
#
# Пример вывода: Белуга fresh

fish = [
    {"specie": "Белуга", "water": "fresh"},
    {"specie": "Карась", "water": "fresh"},
    {"specie": "Красноперка", "water": "fresh"},

    {"specie": "Морской окунь", "water": "sea"},
    {"specie": "Тунец", "water": "sea"},
    {"specie": "Скумбрия", "water": "sea"},
]


def get_fish(label: str) -> tuple[str, str]:
    for each_fish in fish:
        if each_fish["specie"].lower() == label.lower():
            return each_fish["specie"], each_fish["water"]
        else:
            print("Name error. Name not found. Try again")
            return "", ""


# Не удаляйте код ниже, он нужен для проверки!

fish_name = input("fish_name: ")
fish_label, water = get_fish(fish_name)
print(fish_label, water)
