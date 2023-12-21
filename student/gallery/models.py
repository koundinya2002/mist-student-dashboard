from django.db import models

# Create your models here.
class snaps(models.Model):
    snap_name = models.CharField(max_length=255, default="img")
    snap = models.FileField(null=True)
    time = models.DateTimeField(auto_now=True)

    def __str(self):
        return str(self.snap_name)