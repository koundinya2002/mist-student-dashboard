from django.db import models

# Create your models here.
class items(models.Model):
    item_name = models.CharField(max_length=50, default="file")
    item_photo = models.FileField(null=True)
    time = models.DateTimeField(auto_now=True)
    item_desc = models.TextField()

    def __str__(self):
        return str(self.item_name)