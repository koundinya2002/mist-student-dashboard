from django.db import models

# Create your models here.
class notes(models.Model):
    file_name = models.CharField(max_length=50, default="file")
    file = models.FileField(null=True)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file_name)