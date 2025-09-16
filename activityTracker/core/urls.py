from django.urls import path
from . import views

urlpatterns = [
   path("", views.index, name="index"),
   path("new_activity/", views.new_activity, name="new_activity")
]