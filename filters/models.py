from django.db import models
from django.contrib.postgres.indexes import GinIndex
import uuid

CODE_LENGTH = 5

class Filter(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=CODE_LENGTH, unique=True)
    filter = models.JSONField(unique=True)

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        if len(self.code) == 0:
            while True:
                code = uuid.uuid4().hex[:CODE_LENGTH].upper()
                if not Filter.objects.filter(code=code).exists():
                    break
            self.code = code
        super(Filter, self).save(*args, **kwargs)

    class Meta:
        indexes = [
            GinIndex(
                fields=['filter'],
                name='filter_gin',
            ),
        ]