from django.db import models
from django.utils import timezone

# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    edited_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def publish(self):
        self.save()
