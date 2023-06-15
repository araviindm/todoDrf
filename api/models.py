from django.db import models


class TagManager(models.Manager):
    pass


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    objects = TagManager()

    def __str__(self):
        return self.name


class TodoManager(models.Manager):
    pass


class StatusTypes(models.TextChoices):
    OPEN = "OPEN"
    WORKING = "WORKING"
    DONE = "DONE"
    OVERDUE = "OVERDUE"


class Todo(models.Model):
    time_stamp = models.DateTimeField(editable=False, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=False, null=False)
    due_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='todos', blank=True)
    status = models.CharField(max_length=7,
                              choices=StatusTypes.choices,
                              default=StatusTypes.OPEN,
                              blank=False,
                              null=False
                              )
    objects = TodoManager()

    def __str__(self):
        return self.title
