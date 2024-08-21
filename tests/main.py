import unittest
import requests
from unittest import TestCase
from first_task import meeting_a_soul, get_name, get_directory, add, all_mentors, all_names_mentors, unique_sorted_names, mentors
import configparser

config = configparser.ConfigParser()
config.add_section('YANDEX')
config.read('config.ini')
token = config.get('YANDEX', 'key')



class TestMeetingApp(TestCase):
    def test_meeting_a_soul(self):
        boys = ["Иван", "Егор", "Алексей", "Филипп"]
        girls = ["Екатерина", "Мария", "Юлия", "Арина"]
        expected = 'Алексей & Арина, Егор & Екатерина, Иван & Мария, Филипп & Юлия'
        result = meeting_a_soul(boys, girls)
        self.assertEqual(expected, result)

    def test_meeting_a_soul_without_one_girl(self):
        boys = ["Иван", "Егор", "Алексей", "Филипп"]
        girls = ["Екатерина", "Мария", "Юлия"]
        expected = "Кто-то может остаться без пары"
        result = meeting_a_soul(boys, girls)
        self.assertEqual(expected, result)

    def test_meeting_a_soul_without_one_boy(self):
        boys = ["Иван", "Алексей", "Филипп"]
        girls = ["Екатерина", "Мария", "Юлия", "Арина"]
        expected = "Кто-то может остаться без пары"
        result = meeting_a_soul(boys, girls)
        self.assertEqual(expected, result)

"""1.1 оттестился без ошибок"""

class TestSecretary(TestCase):
    def test_get_name(self):
        expected = "Геннадий Покемонов"
        result = get_name("11-2")
        self.assertEqual(expected, result)

    def test_get_name_not_found(self):
        expected = 'Документ не найден'
        result = get_name("5")
        self.assertEqual(expected, result)

    def test_get_directory(self):
        expected = '1'
        result = get_directory('2207 876234')
        self.assertEqual(expected, result)

    def test_get_directory_not_found(self):
        expected = 'Полки с таким документом не найдено'
        result = get_directory('5553535')
        self.assertEqual(expected, result)

    def test_add(self):
        result_1 = add('passport', '45 087 23', 'Алиса Суворова', 3)
        result_2 = get_name('45 087 23')
        expected = 'Алиса Суворова'
        self.assertEqual(expected, result_2)

"""1.2 оттестился без ошибок"""

class TestMentors(TestCase):
    def test_all_mentors(self):
        result = all_mentors()
        expected = set(mentors[0]) | set(mentors[1]) | set(mentors[2]) | set(mentors[3])
        self.assertEqual(expected, result)

    def test_all_names_mentors(self):
        result = len(all_names_mentors())
        expected = 46
        self.assertEqual(result, expected)

    def test_unique_sorted_names(self):
        result = len(unique_sorted_names().split(','))
        expected = 33
        self.assertEqual(result, expected)

"""1.3 оттестился без ошибок"""

class TestYandexDiskApi(TestCase):
    def setUp(self):
        self.headers = {
            'Authorization': f'OAuth {token}'
        }
    def test_with_params(self):
        for i, (param, folder_name, expected) in enumerate([
            ('path', 'My_Images', 201),
            ('path', 'Work', 201),
            ('path', 'Work', 409),
            ('путь', 'Study', 400),
        ]):
            with self.subTest(i):
                params = {
                    param: folder_name
                }
                response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                        params=params,
                                        headers=self.headers)
                result = response.status_code
                self.assertEqual(expected, result)

"""2.1 оттестился без ошибок"""






