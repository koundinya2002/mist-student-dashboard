from django.shortcuts import render, redirect
from .models import Classroom, StudentClassroom, TeacherClassroom, Notifications
from helper import random_str
from itertools import chain
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
# def home(request):
#     return render(request, "dashboard/home.html", {})

@login_required
def home(request):
    return render(request, "dashboard/home.html", {})



@login_required
def view_all_classrooms(request):
    s = StudentClassroom.objects.filter(user=request.user)
    t = TeacherClassroom.objects.filter(user=request.user)
    classrooms = list(chain(s, t))
    return render(request, "dashboard/view_classrooms.html",{
        "classrooms": classrooms
    })



@login_required
def create_classroom(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        join_code = random_str()
        
        c = Classroom.objects.create(title=title, description=description, owner=request.user, join_code=join_code)
        TeacherClassroom.objects.create(user=request.user, classroom=c)

        return redirect("/dashboard/view_classrooms")

    else:
        return render(request, "dashboard/create.html")
    

@login_required
def join_classroom(request):
    if request.method == "POST":
        code = request.POST["code"]
        classroom = Classroom.objects.get(join_code=code)
        StudentClassroom.objects.create(user=request.user, classroom=classroom).pk

        return redirect("/dashboard/view_classrooms")

    else:
        return render(request, "dashboard/join-classroom.html")
    

@login_required
def create_notifications(request):
    if request.method == "POST":
        name = request.POST["name"]
        file2 = request.FILES["file"]
        document = Notifications.objects.create(file_name=name, file=file2)
        document.save()
        return render(request, "dashboard/notified.html")
    return render(request, "dashboard/create_notification.html")


@login_required
def notify(request):
    notifications = Notifications.objects.all()
    return render(request, "dashboard/notifications.html", {
        "files": notifications,
    })