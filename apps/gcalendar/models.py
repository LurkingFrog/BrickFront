from django.db import models
from django_fields.fields import EncryptedCharField

class Calendar(models.Model):
    """
This is a calendar display. It contains the oauth
info needed to manage the master account as well
as the embed info

:Parameter slug: The name by which this should be accessed in the url
:Parameter title: The header on the embedded calendar
:Parameter mode: Whether to display Monthly, Weekly, or Agenda
  views. The default is weekly (WEEK)
:Parameter week_start: The day of the week that the calendar should
  start on. The default is 1 (Sunday)
:Parameter bgcolor: The color of the calendar's background in hex
:Parameter height: Display height in pixels.
:Parameter username: The google username for the account this master
  calendar. Leave this field blank if you don't have access to modify
  it.
:Parameter password: The google password for the account this master
  calendar. Leave this field blank if you don't have access to modify
  it.
    """
    
    slug = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    mode = models.CharField(max_length=20, default='WEEK')
    week_start = models.IntegerField(default=1)
    bgcolor = models.CharField(max_length=6, default='FFFFFF')
    height = models.IntegerField(default=600)
    username = models.CharField(max_length=512, null=True, default='')
    password = EncryptedCharField(max_length=128, null=True, default='')


class Category(models.Model):
    """
    Each one of these corresponds to a different "calendar", though
    all can be displayed in one.
    """
    pass


class Event(models.Model):
    """
    A local copy of the event.

    TODO:
      reconcile with google
    """
    pass


