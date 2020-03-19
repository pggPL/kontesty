from app.models import User
import hashlib
import os


def get_size(start_path='.'):
    """ Returns total size of files in given directory"""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


def current_files(request, context):
    """ Returns list of users(from context) files"""
    if context.get('username') is None:
        return []
    if not os.path.exists('./app/user_solutions/' + context['username']):
        return []
    output = os.listdir('./app/user_solutions/' + context['username'])
    try:
        output.remove(".DS_Store")
    except:
        pass

    return output


def remove_file(username, file):
    """ Removes given file of given user"""
    print('./app/user_solutions/' + username + '/' + file)
    if not os.path.exists('./app/user_solutions/' + username + '/' + file):
        return False
    os.remove('./app/user_solutions/' + username + '/' + file)
    return True


def submit_solutions(request, context):
    """ Is serving solutions submitting to the server"""
    if request.method != 'POST':
        return False
    if request.POST['send_files'] is None:
        return False
    if not Account.is_logged(request):
        return False

    if not os.path.exists('./app/user_solutions/' + context['username']):
        os.mkdir('./app/user_solutions/' + context['username'])

    current_size = get_size('./app/user_solutions/' + context['username'])
    print(current_size)

    for file in request.FILES.getlist('file'):
        for chunk in file.chunks():
            current_size += os.stat('./app/user_solutions/' + context['username']).st_size;
            if current_size > 25000000:
                return "BIG"
            zapis = open('./app/user_solutions/' + context['username'] + '/' + str(file), 'wb+')
            zapis.write(chunk)
            zapis.close()


def check_if_variables_are_set(request, list_of_names):
    """ This function takes list of strings and request
    and checks if all of elements are declared were send by thr POST method"""
    for el in list_of_names:
        if request.POST.get('username') is None:
            return False
    return True


class Account:
    """ This class contains all methods connected to accounts/logging in/registering etc"""
    @staticmethod
    def try_register(request, number_of_problems):
        """ This function is registering an user from request. It returns "Wrong data" if data given by user are
         not complete and returns "OK" if all was ok and user is registered """
        if request.method != "POST":
            return "Wrong data"
        required_data = ['email', 'real_name', 'real_surname', 'school', 'city', 'user_class', 'password', 'username']
        if check_if_variables_are_set(request, required_data):
            return "Wrong data"
        if len(request.POST.get('username')) < 3:
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

        new_user.marks="$".join(['?']*number_of_problems)
        request.session['logged'] = True
        request.session['username'] = request.POST['username']
        request.session['password'] = request.POST['password']

        # Create directory for solutions
        if not os.path.exists('./app/user_solutions/' + request.POST['username']):
            os.mkdir('./app/user_solutions/' + request.POST['username'])

        new_user.save()

        print("Zarejestrowano pomyślnie")
        return "OK"

    @staticmethod
    def try_login(request):
        """ This function is serving logging in. It returns state of this logging in."""
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
        """ Returns true if user is logged, false if not"""
        if request.session.get('logged') is None:
            return False
        if request.session.get('username') is None:
            return False
        if request.session.get('password') is None:
            return False

        querry = User.objects.filter(username=request.session.get('username'))
        password = hashlib.sha1(request.session.get('password').encode()).digest()
        if len(querry) != 1:
            return False
        if str(querry[0].password) != str(password):
            return False
        return True

    @staticmethod
    def logout(request):
        """ Log user out """
        if request.session.get('logged') is not None:
            del request.session['logged']
        if request.session.get('username') is not None:
            del request.session['username']
        if request.session.get('password') is not None:
            del request.session['password']

    @staticmethod
    def update_context(request, context):
        """ Updates the dictionary "context" by new data connected to accounts """
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
        context['admin'] = querry[0].admin
        context['usermarks'] =  zip(range(1, len(querry[0].marks) + 1), querry[0].marks.split('$'))

        return context

    @staticmethod
    def try_change_data(request):
        """ Serves changing data"""
        if not Account.is_logged(request):
            return "User is not logged"
        if request.method != "POST":
            return "Wrong data"
        required_data = ['email', 'real_name', 'real_surname', 'school', 'city', 'user_class', 'password', 'username']
        if check_if_variables_are_set(request, required_data):
            return "Wrong data"
        if len(request.POST.get('username')) < 3:
            return "Wrong data"
        if request.POST['username'] != request.session['username']:
            return "Wrong name"
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
        """ Serves changing password"""
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
