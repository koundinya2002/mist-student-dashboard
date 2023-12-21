from django.contrib import admin
from .models import Classroom, StudentClassroom, TeacherClassroom, Profile, Notifications

# Register your models here.
admin.site.register(Classroom)
admin.site.register(StudentClassroom)
admin.site.register(TeacherClassroom)
admin.site.register(Profile)
admin.site.register(Notifications)


