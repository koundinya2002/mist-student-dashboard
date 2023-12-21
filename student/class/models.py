from django.db import models

# Create your models here.
class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    classroom = models.ForeignKey("dashboard.Classroom", on_delete=models.CASCADE)
    points = models.IntegerField()
    assigned = models.DateTimeField(auto_now=True)
    due = models.DateTimeField(null=True)
    slug = models.SlugField(null=True)

    def __str__(self) -> str:
        return str(self.title) + ' | ' + str(self.classroom)

class Topic(models.Model):
    classroom = models.ForeignKey("dashboard.Classroom", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

