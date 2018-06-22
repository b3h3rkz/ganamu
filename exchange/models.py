from django.db import models
import uuid


class Exchange(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, unique=True)
    url = models.URLField(max_length=100, unique=True, blank=True, null=True)
    logo = models.URLField(max_length=100, unique=True, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="exchange")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
