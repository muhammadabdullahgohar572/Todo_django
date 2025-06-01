from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_task',views.add_task,name="add_task"),
    path('ShowTask',views.ShowTask,name="ShowTask"),

]