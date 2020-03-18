from app.models import User
import hashlib


class Account:
    @staticmethod
    def try_register(request):
        if request.method != "POST":
            return "Wrong data"
        if request.POST.get('username') is None:
            return "Wrong data"
        if len(request.POST.get('username')) < 3:
            return "Wrong data"
        if request.POST.get('email') is None:
            return "Wrong data"
        if request.POST.get('real_name') is None:
            return "Wrong data"
        if request.POST.get('real_surname') is None:
            return "Wrong data"
        if request.POST.get('email') is None:
            return "Wrong data"
        if request.POST.get('school') is None:
            return "Wrong data"
        if request.POST.get('city') is None:
            return "Wrong data"
        if request.POST.get('user_class') is None:
            return "Wrong data"
        if request.POST.get('password') is None:
            return "Wrong data"
        # We check if username is free
        if User.objects.filter(username=request.POST.get('username')).exists():
            return "Username used"
        new_user = User()
        new_user.username = request.POST['username']
        new_user.email = request.POST['email']
        new_user.real_name = request.POST['real_name']
        new_user.real_surname = request.POST['real_surname']
        new_user.school = request.POST['school']
        new_user.city = request.POST['city']
        new_user.user_class = request.POST['user_class']
        hash_object = hashlib.sha1(request.POST['password'].encode())
        new_user.password = hash_object.digest()
        new_user.save()
        print("Zarejestrowano pomyślnie")
        return "OK"

    @staticmethod
    def try_login(request):
        # Check if is logged by session
        if request.session.get('logged') is not None:
            return "Already logged"
        # If not, check log data

        if request.method != "POST":
            return "Wrong data"
        if request.POST.get('username') is None:
            return "Wrong data"
        if request.POST.get('password') is None:
            return "Wrong data"
        password = hashlib.sha1(request.POST['password'].encode()).digest()
        querry = User.objects.filter(username=request.POST['username'])

        if not querry.exists():
            return "Wrong password"
        print(querry[0].password)
        print(password)
        if str(querry[0].password) != str(password):
            return "Wrong password";

        # Tutaj cała procedura logowania

        request.session['username'] = request.POST['username']
        request.session['password'] = request.POST['password']
        request.session['logged'] = True

        return "OK"

    @staticmethod
    def is_logged(request):
        if request.session.get('logged') is None:
            return False
        if request.session.get('username') is None:
            return False
        if request.session.get('password') is None:
            return False

        querry = User.objects.filter(username=request.session.get('username'))
        password = hashlib.sha1(request.session.get('password').encode()).digest()
        if str(querry[0].password) != str(password):
            return False
        return True

    @staticmethod
    def logout(request):
        if request.session.get('logged') is not None:
            del request.session['logged']
        if request.session.get('username') is None:
            del request.session['username']
        if request.session.get('password') is None:
            del request.session['password']

    @staticmethod
    def update_context(request, context):
        if request.session.get('logged') is None:
            return context
        if request.session.get('username') is None:
            return context
        if request.session.get('password') is None:
            return context

        querry = User.objects.filter(username=request.session.get('username'))
        password = hashlib.sha1(request.session.get('password').encode()).digest()
        if str(querry[0].password) != str(password):
            return context

        context['username'] = querry[0].username
        context['real_name'] = querry[0].real_name
        context['email'] = querry[0].email
        context['real_surname'] = querry[0].real_surname
        context['city'] = querry[0].city
        context['school'] = querry[0].school
        context['user_class'] = querry[0].user_class

        return context

    @staticmethod
    def try_change_data(request):
        if not Account.is_logged(request):
            return "User is not logged"
        if request.method != "POST":
            return "Wrong data"
        if request.POST.get('username') is None:
            return "Wrong data"
        if len(request.POST.get('username')) < 3:
            return "Wrong data"
        if request.POST['username'] != request.session['username']:
            return "Wrong name"
        if request.POST.get('email') is None:
            return "Wrong data"
        if request.POST.get('real_name') is None:
            return "Wrong data"
        if request.POST.get('real_surname') is None:
            return "Wrong data"
        if request.POST.get('email') is None:
            return "Wrong data"
        if request.POST.get('school') is None:
            return "Wrong data"
        if request.POST.get('city') is None:
            return "Wrong data"
        if request.POST.get('user_class') is None:
            return "Wrong data"
        # We check if username is free
        try:
            user_to_change = User.objects.get(username=request.POST.get('username'))
            user_to_change.username = request.POST['username']
            user_to_change.email = request.POST['email']
            user_to_change.real_name = request.POST['real_name']
            user_to_change.real_surname = request.POST['real_surname']
            user_to_change.school = request.POST['school']
            user_to_change.city = request.POST['city']
            user_to_change.user_class = request.POST['user_class']
            user_to_change.save()
        except:
            print("User is not registered")
            return False

        print("Zarejestrowano pomyślnie")
        return True

    @staticmethod
    def try_change_password(request):
        if not Account.is_logged(request):
            return "User is not logged"
        if request.method != "POST":
            return "Wrong data"
        if request.POST.get('old_password') is None:
            return "Wrong data"
        if request.POST.get('new_password') is None:
            return "Wrong data"
        if str(request.POST.get('old_password')) != str(request.session['password']):
            return "Fatal error"
        print("xx")
        # We check if username is free
        try:
            user_to_change = User.objects.get(username=request.POST.get('username'))
            user_to_change.password = hashlib.sha1(request.POST['new_password'].encode()).digest()

            user_to_change.save()
        except:
            print("User is not registered")
            return False

        print("Zarejestrowano pomyślnie")
        return True
