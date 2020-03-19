from app.login import *
from app.models import *
from datetime import datetime, timedelta
from django.utils import timezone


def set_context(request):
    """ Returns dictionary "context" in which are main settings of user as its username, password and
    settings of program as number of problems. This dictionary is used later to render templates."""
    output = {'logged': False}
    if Account.is_logged(request):
        output['logged'] = True
        Account.update_context(request, output)
    output['contest_name'] = Settings.objects.filter().get().contest_name
    output['main_content'] = Settings.objects.filter().get().main_page_content
    output['rules'] = Settings.objects.filter().get().rules.split(';')
    output['number_of_problems_value'] = Settings.objects.filter().get().number_of_problems
    output['number_of_problems'] = range(1, Settings.objects.filter().get().number_of_problems + 1)
    con_start = Settings.objects.filter().get().constest_start
    duration = Settings.objects.filter().get().contest_duration_in_minutes
    output['mark_view'] = Settings.objects.filter().get().mark_view
    today = timezone.now()
    output['contest_in_progress'] = False
    output['contest_finished'] = False
    con_start=con_start.replace(tzinfo=None)
    today=today.replace(tzinfo=None)
    output['contest_start_date']=(con_start-datetime(1970,1,1,1)).total_seconds()*1000;
    output['contest_end_date']=(con_start+timedelta(minutes=duration)-datetime(1970,1,1)).total_seconds()*1000;
    if con_start < today < con_start + timedelta(minutes=duration):
        output['contest_in_progress'] = True
    elif today > con_start + timedelta(minutes=duration):
        output['contest_finished'] = True

    return output
