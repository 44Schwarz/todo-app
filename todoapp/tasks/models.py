from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Goals will be in tasks app in order to link tasks to certain goals. Goals will be like top-level projects
# Create your models here.
class Goal(models.Model):
    name = models.CharField(max_length=30)
    completed = models.BooleanField(default=False)
    was_completed_at = models.DateField(blank=True)
    to_be_completed_by = models.DateField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=30)
    goal = models.ForeignKey(Goal, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    text = models.CharField(max_length=80)
    comment = models.TextField(blank=True)
    link = models.URLField(blank=True)
    was_completed_at = models.DateField(blank=True)
    to_be_completed_by = models.DateField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, default='Inbox')  # TODO default doesn't work
    recurring = models.BooleanField()
    repeat_at = models.DateTimeField(blank=True)
    priority = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return '{} — {}'.format(self.text, self.project)
