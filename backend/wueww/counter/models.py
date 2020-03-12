from django.db import models


class Counter(models.Model):
    value = models.IntegerField()
