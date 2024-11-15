from django.db import models


class Tasks(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
