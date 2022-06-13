from django.db import models

# Create your models here.
class Embassy(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    hours = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    location = models.URLField()

    def __str__(self):
        return self.name