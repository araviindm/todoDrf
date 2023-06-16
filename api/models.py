from django.db import models
from rest_framework.authtoken.models import Token


class TodoManager(models.Manager):
    pass


class StatusTypes(models.TextChoices):
    OPEN = "OPEN"
    WORKING = "WORKING"
    DONE = "DONE"
    OVERDUE = "OVERDUE"


class Todo(models.Model):
    time_stamp = models.DateTimeField(editable=False, blank=False, null=False, auto_now_add=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=1000, blank=False, null=False)
    due_date = models.DateTimeField(blank=True, null=True)
    tags = models.CharField(max_length=1000,
                            blank=True,
                            null=True,
                            help_text='The format is ["sample_tag","sample"]'
                            )
    status = models.CharField(max_length=7,
                              choices=StatusTypes.choices,
                              default=StatusTypes.OPEN,
                              blank=False,
                              null=False
                              )
    objects = TodoManager()

    def __str__(self):
        return self.title

