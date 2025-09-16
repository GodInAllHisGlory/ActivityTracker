from django.shortcuts import render
from .models import Activity, TimeLog

# Create your views here.
def index(req):
    return render(req, "core/index.html")

def new_activity(req):
    return render(req, "core/new_activity.html")