from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from .models import Activity, TimeLog
from datetime import datetime

# Create your views here.
def index(req: HttpRequest):
    activities = Activity.objects.all()
    return render(req, "core/index.html", {"activities": activities})

def activity(req: HttpRequest, id):
    activity = Activity.objects.get(id=id)
    return render(req, "core/activity.html", {"activity": activity})

def new_activity(req: HttpRequest):
    return render(req, "core/new_activity.html")

def new_timelog(req: HttpRequest, id):
    activity = Activity.objects.get(id=id)
    return render(req, "core/new_timelog.html", {"activity": activity})

def create_activity(req: HttpRequest):
    query = req.POST
    name = query.get("name", "New Activity")
    activity = Activity(
        name = name
    )
    activity.save()
    return redirect("/")

def create_timelog(req: HttpRequest, id):
    activity = Activity.objects.get(id=id)
    query = req.POST
    start = datetime.strptime(query.get("start-time"), '%Y-%m-%dT%H:%M')
    end = datetime.strptime(query.get("end-time"), '%Y-%m-%dT%H:%M')
    print(f"Start Time: {start}")
    print(f"End Time: {end}")
    return redirect(f"/activity/{id}")



