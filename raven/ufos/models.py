import datetime
from django.db import models
from django.utils import timezone

class Event(models.Model):
    event_text = models.CharField(max_length=200)
    event_description = models.CharField(max_length=200, blank=True, default="")
    # event_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event_text

    @property
    def last_update(self):
        return self.updated_at >= timezone.now() - datetime.timedelta(days=7)

class Location(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    location_text = models.CharField(max_length=200)

    def __str__(self):
        return self.location_text

