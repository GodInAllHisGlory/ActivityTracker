from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Activity, TimeLog
from datetime import datetime

def index(req: HttpRequest):
    activities = Activity.objects.all()
    return render(req, "core/index.html", {"activities": activities})

#Gets the activity object and all its associated timelog objects
def activity(req: HttpRequest, id):
    activity = Activity.objects.get(id=id)
    timelogs = activity.timelog_set.all()
    return render(req, "core/activity.html", {
        "activity": activity,
        "timelogs": timelogs
        })

def new_activity(req: HttpRequest):
    return render(req, "core/new_activity.html")

def new_timelog(req: HttpRequest, id):
    activity = Activity.objects.get(id=id)
    return render(req, "core/new_timelog.html", {"activity": activity})

#Creates the activity object and sends you back to the index
def create_activity(req: HttpRequest):
    query = req.POST
    name = query.get("name", "New Activity")
    activity = Activity(
        name = name
    )
    activity.save()
    return redirect("/")

#Creates a TimeLog object
def create_timelog(req: HttpRequest, id):
    activity_key = Activity.objects.get(id=id)
    query = req.POST
    start = datetime.strptime(query.get("start-time"), '%Y-%m-%dT%H:%M')
    end = datetime.strptime(query.get("end-time"), '%Y-%m-%dT%H:%M')
    timelog = TimeLog(
        start_time = start,
        end_time = end,
        log = activity_key
    )
    timelog.save()
    return redirect(f"/activity/{id}")



