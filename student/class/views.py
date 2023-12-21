from django.shortcuts import render,redirect
from django.http import HttpResponse
from dashboard.models import Classroom, StudentClassroom, TeacherClassroom
from datetime import datetime
from django.urls import reverse_lazy
from .models import Assignment
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def index(request, class_id):
    classroom = Classroom.objects.get(join_code=class_id)
    assignments = Assignment.objects.filter(classroom=classroom)
    
    return render(request, 'class/index.html', {
        "assignments": assignments,
        "classroom": classroom
    })


@login_required
def post_assignment(request, class_id):
    classroom = Classroom.objects.get(join_code=class_id)
    if request.method == "POST":
        date_time_obj = datetime.strptime(request.POST.get("due"), '%Y-%m-%dT%H:%M')
        assignment = Assignment.objects.create(title=request.POST.get("title"), description=request.POST.get("description"), classroom=classroom, points=request.POST.get("points"), due=date_time_obj, slug=slugify(request.POST["title"]))
        # ordering = ['-assignment.due']
        return render(request, "class/assigned.html",{
            "classroom":Classroom.objects.get(join_code=class_id)
        })
    else:
        return render(request, "class/post-assignment.html",{
            "classroom": classroom
        })
    
    

@login_required
def view_assignment(request, class_id, assignment_slug):
    classroom = Classroom.objects.get(join_code=class_id)
    assignment = Assignment.objects.get(classroom=classroom, slug=assignment_slug)
    role = ""

    try:
        tc = TeacherClassroom.objects.get(classroom=classroom, user=request.user)
        role = "teacher"
    except TeacherClassroom.DoesNotExist:
        sc = StudentClassroom.objects.get(classroom=classroom, user=request.user)
        role = "student"

    return render(request, "/class/view-assignment_student.html", {
        "role": role,
    })


@login_required
def classmates(request, class_id):
    return render(request, "class/classmates.html", {})