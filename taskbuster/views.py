import datetime
from django.shortcuts import render
from django.utils.timezone import now


def home(request):
    return render(request, "taskbuster/index.html",
        {"today": datetime.date.today(), "now": now()})

def home_files(request, filename):
    return render(request, filename, {}, content_type='text/plain')
