from django.conf import settings
from django.db import models
from django_extensions.db.fields import json


class Dataset(models.Model):
    # nullable because we don't really care who owns it, but should be set
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.owner or 'anonymous'


class Datapoint(models.Model):
    dataset = models.ForeignKey(Dataset, related_name='datapoints')

    name = models.CharField(max_length=255, unique=True)
    meta = json.JSONField()

    # match
    match = models.ForeignKey('self', related_name='+', null=True, blank=True)
    match_confidence = models.FloatField(null=True, blank=True,
        help_text='How confident are we that this match is right?')
    match_won = models.PositiveIntegerField(default=0,
        help_text='How many times the match was chosen')
    match_sample = models.PositiveIntegerField(default=0,
        help_text='How many times this question was asked')

    # bookkeeping fields
    created_at = models.DateTimeField(auto_now_add=True)
    created_from = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Question(models.Model):
    """
    Asks a question about a datapoint in a dataset.
    """
    datapoint = models.OneToOneField(Datapoint, null=True, blank=True,
        related_name='question')
    includes = models.CommaSeparatedIntegerField(max_length=100,
        help_text='These are PKs of the `Datapoint`s the '
        'question should prefer to offer as choices.')
    excludes = models.CommaSeparatedIntegerField(
        max_length=255,
        help_text='These `Datapoint` PKs should be excluded '
        'as answer choices.')


class Response(models.Model):
    """
    Every response to a `Question`.
    """
    question = models.ForeignKey(Question)
    choice = models.ForeignKey(Datapoint)

    # bookkeeping
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=48)
    user_agent = models.CharField(max_length=200)
