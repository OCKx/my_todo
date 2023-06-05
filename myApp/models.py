from django.db import models

# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=20)
    pin = models.IntegerField()

    def __str__(self):
        return self.username
    


class ListItem(models.Model):
    list = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.list