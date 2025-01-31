"""Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек (их число может варьироваться):
Выдвигаем гипотезу: мы получим лучшие рекомендации, если просто отсортируем имена по алфавиту
и познакомим людей с одинаковыми индексами после сортировки.
Если количество людей в списках будет не совпадать, то мы никого не будем знакомить и выведем пользователю предупреждение,
что кто-то может остаться без пары."""

boys = ["Иван", "Егор", "Алексей", "Филипп"]
girls = ["Екатерина", "Мария", "Юлия", "Арина"]

def meeting_a_soul(boys: list, girls: list):
    result = ''
    if len(boys) == len(girls):
        for b, g in zip(sorted(boys), sorted(girls)):
            result += f'{b} & {g}, '
        result = result[:-2]
    else:
        result = 'Кто-то может остаться без пары'
    return result


"""Я работаю секретарём, и мне постоянно приходят различные документы. 
Я должен быть очень внимателен, чтобы не потерять ни один документ. 
Необходимо реализовать следующие функции.
get_name — функция. Принимает номер документа и выводит имя человека, которому он принадлежит. 
Если такого документа не существует, вывести “Документ не найден”.
get_directory — функция. Принимает номер документа и выводит номер полки, на которой он находится. 
Если такой документ не найден, на полках вывести “Полки с таким документом не найдено”.
add — функция, которая добавит новый документ в каталог и перечень полок."""

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def get_name(doc_number):
    for document in documents:
        if document['number'] in doc_number:
            return document['name']
    if document['number'] not in doc_number:
        return 'Документ не найден'


def get_directory(doc_number):
    for shelf_number, doc_numbers in directories.items():
        if doc_number in doc_numbers:
            return shelf_number
    if doc_number not in doc_numbers:
        return 'Полки с таким документом не найдено'


def add(document_type, number, name, shelf_number):
    documents.append({"type": document_type, "number": number, "name": name})
    if shelf_number in directories:
        directories[shelf_number].append(number)
    else:
        directories[shelf_number] = [number]

"""У нас есть 4 курса Нетологии, на которых преподают 4 группы преподавателей.
Задача — отделить имена от фамилий и собрать все имена преподавателей со всех четырёх курсов.
Имена ни в коем случае не должны повторяться. 
А чтобы всё было красиво, отсортировать их в алфавитном порядке.
"""

courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Frontend-разработчик с нуля"]

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

def all_mentors():
    Python = set(mentors[0])
    Java = set(mentors[1])
    Fullstack = set(mentors[2])
    Fronted = set(mentors[3])
    all_list = (Python | Java | Fullstack | Fronted)
    return all_list


def all_names_mentors():
    all_names_list = []
    for mentor in all_mentors():
        name = mentor.split()[0]
        all_names_list.append(name)
    return all_names_list

not_unique_names = all_names_mentors()
def unique_sorted_names():
    unique_name = set(not_unique_names)
    all_names_sorted = sorted(unique_name)
    string_name = ', '.join(all_names_sorted)
    return string_name 