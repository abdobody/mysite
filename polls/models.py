import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


# Create your models here.


@python_2_unicode_compatible
class Content(models.Model):
    type = models.CharField(max_length=200, blank=False, null=False)
    media_type = models.CharField(max_length=40, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    subject = models.CharField(max_length=100, blank=False, null=False)
    scene = models.CharField(max_length=200)
    genre = models.CharField(max_length=100, blank=False, null=False)
    language = models.CharField(max_length=100, blank=False, null=False)
    location = models.CharField(max_length=50)
    date_create = models.DateTimeField('date created')

    def was_published_recently(self):
        return self.date_create >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Asset(models.Model):
    clip_code = models.ForeignKey(Content, on_delete=models.CASCADE)
    creator_role = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100, blank=False, null=False)
    rights = models.CharField(max_length=50)

    def __str__(self):
        return self.creator_role


@python_2_unicode_compatible
class Proberty(models.Model):
    duration = models.CharField(max_length=100)
    physical_format = models.CharField(max_length=50, blank=False, null=False)
    digital_format = models.CharField(max_length=20, blank=False, null=False)
    encoding = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.encoding
