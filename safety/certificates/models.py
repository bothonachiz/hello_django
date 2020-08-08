from django.db import models


class Certificate(models.Model):
    name = models.CharField(max_length=50)
    issue_by = models.CharField(max_length=50)
