from django.test import TestCase

# Create your tests here.

from django.test import TestCase, Client
from app.models import User, Settings
import datetime


class UserTest(TestCase):
    def set_up(self):
        pass

    def test_1(self):
        maciek = User()
        maciek.username = "a"
        maciek.password = "a"
        maciek.user_class = 8
        maciek.city = "a"
        maciek.real_surname = "a"
        maciek.email = "a"
        maciek.school = "a"
        maciek.real_name = "a"

    def test_2(self):
        c = Client()
        s = Settings()
        s.contest_name = "a"
        s.number_of_problems = 5
        s.constest_start = datetime.datetime(year=2020, month=10, day=5)
        s.main_page_content = "a"
        s.rules = "a"
        s.contest_duration_in_minutes = 180
        s.save()

        response = c.get('/index/')
        response = c.get('/user/')
        response = c.get('/register')
        response = c.get('/rules')
        response = c.get('/user_settings')
        response = c.get('/logout')
        response = c.get('/login')
        response = c.get('/change_password')
        response = c.get('/problems')
        response = c.get('/user_file')
        response = c.get('/remove')
        response = c.get('/remove')
        response = c.get('check_panel')
        response = c.get('update_check')
        response = c.get('change_check')
        response = c.get('solutions_check')
        response = c.get('display_image_check')
        response = c.get('remove')

