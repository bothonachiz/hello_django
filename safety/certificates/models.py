from django.db import models

from workers.models import Worker


class Certificate(models.Model):
    name = models.CharField(max_length=50)
    issue_by = models.CharField(max_length=50)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
