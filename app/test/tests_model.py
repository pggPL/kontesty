from django.test import TestCase, Client
from app.models import User, Settings
import datetime


class ModelTests(TestCase):
    @staticmethod
    def test_user():
        maciek = User()
        maciek.username = "a"
        maciek.password = "a"
        maciek.user_class = 8
        maciek.city = "a"
        maciek.real_surname = "a"
        maciek.email = "a"
        maciek.school = "a"
        maciek.real_name = "a"
        maciek.save()
        maciek.delete()

    @staticmethod
    def test_empty_settings():
        set_test = Settings()
        set_test.number_of_problems = 5
        set_test.contest_duration_in_minutes = 200
        set_test.rules = ""
        set_test.main_page_content = ""
        set_test.constest_start = datetime.datetime(2020, 1, 1, 1)
        set_test.contest_name = ""
        set_test.mark_view = False
        set_test.open_enrollment = True
        set_test.marks_adnotation = ""
        set_test.save()
        set_test.delete()

    @staticmethod
    def test_settings():
        set_test = Settings()
        set_test.number_of_problems = 5
        set_test.contest_duration_in_minutes = 200
        set_test.rules = "aa;aa;aa"
        set_test.main_page_content = "sample 1"
        set_test.constest_start = datetime.datetime(2020, 1, 1, 1)
        set_test.contest_name = "Sample name"
        set_test.mark_view = False
        set_test.open_enrollment = True
        set_test.marks_adnotation = "adn"
        set_test.save()
        set_test.delete()
