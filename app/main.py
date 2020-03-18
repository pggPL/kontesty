from app.login import *
from app.models import *
from datetime import datetime, timedelta
from django.utils import timezone


def set_context(request):
    output = {'logged': False}
    if Account.is_logged(request):
        output['logged'] = True
        Account.update_context(request, output)
    output['contest_name'] = Settings.objects.filter().get().contest_name;
    output['main_content'] = Settings.objects.filter().get().main_page_content;
    output['rules'] = Settings.objects.filter().get().rules.split(';');
    con_start = Settings.objects.filter().get().constest_start;
    duration = Settings.objects.filter().get().contest_duration_in_minutes;
    today = timezone.now()
    output['contest_in_progress'] = False
    output['contest_finished'] = False
    con_start=con_start.replace(tzinfo=None)
    today=today.replace(tzinfo=None)
    print(con_start);
    print(datetime(1900,1,1,1));
    output['contest_start_date']=(con_start-datetime(1970,1,1,1)).total_seconds()*1000;
    output['contest_end_date']=(con_start+timedelta(minutes=duration)-datetime(1970,1,1,1)).total_seconds()*1000;
    print(output['contest_start_date'])
    if con_start < today < con_start + timedelta(minutes=duration):
        output['contest_in_progress'] = True
        print("Contest in progress")
    elif today > con_start + timedelta(minutes=duration):
        output['contest_finished'] = True
        print("Contest in progress")

    print(today + timedelta(minutes=300))

    return output
