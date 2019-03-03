from django.db.models import DateTimeField, FileField, BooleanField
from django.db import models


# Modelo base
class BaseAppModel(models.Model):
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    status = BooleanField(default=True)

    class Meta:
        abstract = True
