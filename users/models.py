import uuid
from django.db import models


class Counter(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False,null=True,blank=True)
    key = models.CharField(null=True, blank=True, max_length=100)
    value = models.BigIntegerField(null=True,blank=True)

    def __str__(self):
        return self.key