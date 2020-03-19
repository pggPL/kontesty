from app.models import User


def load_marks(context):
    """ Load all marks of an current user to contest dictionary. Returns list of marks. """
    output = []
    output_names = []
    for user in User.objects.filter():
        if user.admin:
            continue
        user_marks = user.marks.split('$')
        output.extend(user_marks)
        output_names.append(user.username)
    context['marks'] = output
    context['names'] = output_names
    return True


def change_mark(name, problem, mark):
    """ Changes mark of arbitrary problem of arbitrary user"""
    user = User.objects.filter(username=name)
    if len(user) != 1:
        return False
    marks = user[0].marks.split('$')
    print(marks)
    marks[int(problem)-1] = mark
    user[0].marks = "$".join(marks)
    user[0].save()
    return True
