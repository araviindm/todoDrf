from django.db import models
from django.utils import timezone


# Create your models here.

class Todo(models.Model):
    time_stamp = models.DateTimeField(default=timezone.now, editable=False, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=False, null=False)
    due_date = models.DateTimeField(blank=True, null=False)

    class Tag(models.Model):
        name = models.CharField(max_length=255)

    tag = models.ManyToManyField(Tag, blank=True)

    class StatusTypes(models.TextChoices):
        OPEN = "OPEN"
        WORKING = "WORKING"
        DONE = "DONE"
        OVERDUE = "OVERDUE"

    status = models.CharField(max_length=7,
                              choices=StatusTypes.choices,
                              default=StatusTypes.OPEN,
                              blank=False,
                              null=False
                              )
