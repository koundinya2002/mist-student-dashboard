from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Classroom(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    join_code = models.CharField(max_length=7)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
    

class Profile(models.Model):
    options = [('teacher','teacher'), ('student', 'student')]
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    role = models.CharField(max_length=7, choices=options, default="student")

    def __str__(self):
        return str(self.user) + ' | ' + str(self.role)
    

class StudentClassroom(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    classroom = models.ForeignKey("Classroom", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ' | ' + str(self.classroom)


class TeacherClassroom(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    classroom = models.ForeignKey("Classroom", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ' | ' + str(self.classroom) #+ ' | ' + str(self.user.profile.role)
    

class Notifications(models.Model):
    file_name = models.CharField(max_length=50, default="file")
    file = models.FileField(null=True, blank=True)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file_name) 
