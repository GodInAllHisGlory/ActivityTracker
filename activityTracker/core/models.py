from django.db import models
from datetime import timedelta

# Create your models here.
class Activity(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    
    def activity_time(self):
        delta = timedelta()
        for timelog in self.timelog_set.all():
            delta += (timelog.end_time - timelog.start_time)

        return str(delta)

class TimeLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_time = models.DateField()
    end_time = models.DateField()
    activity = models.ForeignKey("Activity", on_delete=models.CASCADE, name="log")

    def time_spent(self):
        return self.end_time - self.start_time