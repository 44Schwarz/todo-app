from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class List(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default='Inbox', blank=True)  # TODO default doesn't work

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=80, blank=True)
    comment = models.TextField(blank=True)
    list = models.ForeignKey(List, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True)  # TODO does an item need a category?

    def __str__(self):
        return self.name
