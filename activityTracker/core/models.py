from django.db import models

# Create your models here.
class Activity(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    
    def activityTime(self):
        return "Infinity Hours?!?!?!?"

class TimeLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_time = models.DateField()
    end_time = models.DateField()
    activity = models.ForeignKey("Activity", on_delete=models.CASCADE, name="log")