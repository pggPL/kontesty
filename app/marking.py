from app.models import User


def load_marks(context):
    """ Load all marks of an current user to contest dictionary. Returns list of marks. """
    output = []
    output_names = []
    output_sums = []
    for user in User.objects.filter():
        if user.admin:
            continue
        user_marks = user.marks.split('$')
        output.extend(user_marks)
        user_sum = 0
        for mark in user_marks:
            if mark not in ['?', '-']:
                user_sum += int(mark)
        output_sums.append(user_sum)
        output_names.append(user.username)

    context['sums'] = output_sums
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
