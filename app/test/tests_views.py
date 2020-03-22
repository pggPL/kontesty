from django.test import TestCase, Client
from app.models import User, Settings
import datetime
from app.test.tests_model import *
from app.login import Account


class ViewsTests(TestCase):
    def set_up(self):
        set_test = Settings()
        set_test.number_of_problems = 5
        set_test.contest_duration_in_minutes = 200
        set_test.rules = "aa;aa;aa"
        set_test.main_page_content = "sample 1"
        set_test.constest_start = datetime.datetime(2020, 1, 1, 1)
        set_test.contest_name = "Sample xx"
        set_test.mark_view = False
        set_test.open_enrollment = True
        set_test.marks_adnotation = "adn"
        set_test.save()

    def clean_up(self):
        set_test = Settings.objects.filter().get()
        set_test.delete()

    def test_empty_views(self):
        c = Client()
        s = Settings()
        s.contest_name = "a"
        s.number_of_problems = 5
        s.constest_start = datetime.datetime(year=2020, month=10, day=5)
        s.main_page_content = "a"
        s.rules = "a"
        s.contest_duration_in_minutes = 180
        s.open_enrollment = False
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
        s.delete()

    def try_register(self, dictionary):
        c = Client()
        response = c.post('/register', dictionary)
        if len(User.objects.filter(username=dictionary['username'])) != 0:
            print(User.objects.filter(username=dictionary['username'])[0].username)
            print("It is possible to create user without all data!")
            raise AssertionError()

    def test_registering(self):
        self.set_up()
        c = Client()
        response = c.post('/register',
                          {
                              'class': 8,
                              'email': 'mail_testowy',
                              'real_name': 'Jan',
                              'real_surname': 'Kowalski',
                              'city': 'Warsaw',
                              'password': 'afrvdrvdfgvdf',
                              'admin': False,
                              'marks': '0$0$0$0$0'
                          })
        if len(User.objects.filter(password='afrvdrvdfgvdf')) != 0:
            print(User.objects.filter(username='user_unit_test'))
            print("It is possible to create user only with username!")
            raise AssertionError()

        self.try_register({
            'username': 'test_user',
            'user_class': 8,
            'email': 'mail_testowy',
            'real_name': 'Jan',
            'real_surname': 'Kowalski',
            'city': 'Warsaw',
            'password': 'afrvdrvdfgvdf',
            'admin': False,
            'marks': '0$0$0$0$0'
        })
        self.try_register({
            'username': 'test_user',
            'user_class': 8,
            'email': 'mail_testowy',
            'real_name': 'Jan',
            'real_surname': 'Kowalski',
            'city': 'Warsaw',
            'password': 'afrvdrvdfgvdf',
            'admin': False,
            'school': 'sch'
        })
        self.try_register({
            'username': 'test_user',
            'user_class': 8,
            'email': 'mail_testowy',
            'real_name': 'Jan',
            'real_surname': 'Kowalski',
            'city': 'Warsaw',
            'admin': False,
            'marks': '0$0$0$0$0',
            'school': 'sch'
        })
        self.try_register({
            'username': 'test_user',
            'user_class': 8,
            'email': 'mail_testowy',
            'real_name': 'Jan',
            'real_surname': 'Kowalski',
            'password': 'afrvdrvdfgvdf',
            'admin': False,
            'marks': '0$0$0$0$0',
            'school': 'sch'
        })
        self.try_register({
            'username': 'test_user',
            'user_class': 8,
            'email': 'mail_testowy',
            'real_name': 'Jan',
            'city': 'Warsaw',
            'password': 'afrvdrvdfgvdf',
            'admin': False,
            'marks': '0$0$0$0$0',
            'school': 'sch'
        })
        self.try_register({
            'username': 'test_user',
            'user_class': 8,
            'email': 'mail_testowy',
            'real_surname': 'Kowalski',
            'city': 'Warsaw',
            'password': 'afrvdrvdfgvdf',
            'admin': False,
            'marks': '0$0$0$0$0',
            'school': 'sch'
        })
        self.try_register({
            'username': 'test_user',
            'user_class': 8,
            'real_name': 'Jan',
            'real_surname': 'Kowalski',
            'city': 'Warsaw',
            'password': 'afrvdrvdfgvdf',
            'admin': False,
            'marks': '0$0$0$0$0',
            'school': 'sch'
        })
        self.try_register({
            'username': 'test_user',
            'email': 'mail_testowy',
            'real_name': 'Jan',
            'real_surname': 'Kowalski',
            'city': 'Warsaw',
            'password': 'afrvdrvdfgvdf',
            'admin': False,
            'marks': '0$0$0$0$0',
            'school': 'sch'
        })

        # Try to register correct user
        response = c.post('/register',
                          {
                              'username': 'test_user',
                              'user_class': 8,
                              'email': 'mail_testowy',
                              'real_name': 'Jan',
                              'real_surname': 'Kowalski',
                              'city': 'Warsaw',
                              'password': 'afrvdrvdfgvdf',
                              'admin': False,
                              'marks': '0$0$0$0$0',
                              'school': 'I LO'
                          })

        if len(User.objects.filter(city='Warsaw')) == 0:
            print("Creating new user does not work!")
            raise AssertionError()

        self.clean_up()

    def test_log_in(self):
        self.set_up()
        c = Client()
        if c.session.get('logged') is not None:
            raise AssertionError()
        response = c.post('/register',
                          {
                              'username': 'test_user',
                              'user_class': 8,
                              'email': 'mail_testowy',
                              'real_name': 'Jan',
                              'real_surname': 'Kowalski',
                              'city': 'Warsaw',
                              'password': 'afrvdrvdfgvdf',
                              'admin': False,
                              'marks': '0$0$0$0$0',
                              'school': 'I LO'
                          })

        response = c.post('/login', {'username': 'test_user', 'password': 'afrvdrvdfgvdf'})
        if c.session.get('logged') is None:
            raise AssertionError()
        if c.session.get('username') != 'test_user' or c.session.get('password') != 'afrvdrvdfgvdf':
            raise AssertionError()
        c.session['logged'] = None
        c.session['username'] = None
        c.session['password'] = None

        User.objects.filter()[0].delete()
        self.clean_up()

    def test_log_out(self):
        self.set_up()
        c = Client()
        response = c.post('/register',
                          {
                              'username': 'test_user',
                              'user_class': 8,
                              'email': 'mail_testowy',
                              'real_name': 'Jan',
                              'real_surname': 'Kowalski',
                              'city': 'Warsaw',
                              'password': 'afrvdrvdfgvdf',
                              'admin': False,
                              'marks': '0$0$0$0$0',
                              'school': 'I LO'
                          })

        response = c.post('/login', {'username': 'test_user', 'password': 'afrvdrvdfgvdf'})

        response = c.post('/logout', {})

        if c.session.get('logged') is not None:
            raise AssertionError()

        User.objects.filter()[0].delete()
        self.clean_up()
