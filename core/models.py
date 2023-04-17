from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=250)
    priority = models.IntegerField()
    date=models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)


    def __str__(self):
        return self.name
