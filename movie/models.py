import uuid
from django.db import models

class Collection(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Movie(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    genres = models.CharField(max_length=100, null=True, blank=True)  
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title
