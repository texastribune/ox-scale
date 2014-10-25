from __future__ import unicode_literals

from django.db import models
from django_extensions.db.fields.json import JSONField


class QuestionSet(models.Model):
    name = models.CharField(max_length=255, blank=True)
    # XXX shim to get a file input in the Django Admin
    input_file = models.FileField(null=True, blank=True)
    # owner = # TODO
    # Bookkeeping Fields
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{} ({})'.format(self.name, self.questions.count())


class Choice(models.Model):
    set = models.ForeignKey(QuestionSet, related_name='choices')
    choice = models.CharField(max_length=255)

    def __unicode__(self):
        return self.choice


class Question(models.Model):
    """
    Asks a question.
    """
    set = models.ForeignKey(QuestionSet, related_name='questions')
    question = models.TextField()
    choices = models.ManyToManyField(Choice)
    order_matters = models.BooleanField(default=False,
        help_text='Does order matter when displaying choices?')

    def __unicode__(self):
        return self.question


class Response(models.Model):
    """
    Every response to a `Question`.
    """
    question = models.ForeignKey(Question,
        help_text='What question was asked?')
    # Don't bother with M2M and through table b/c we don't interpret responses
    choices_picked = models.CommaSeparatedIntegerField(max_length=255)

    # bookkeeping
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(max_length=48,
        null=True, blank=True)
    meta = JSONField(null=True, blank=True,
        help_text='User-Agent and any other info you might want for later')

    def __unicode__(self):
        # TODO
        return unicode(self.question)

    # CUSTOM PROPERTIES #

    @property
    def choices(self):
        """Pretend we had a .choices m2m field."""
        # TODO perf
        # TODO mimic queryset
        return [Choice.objects.get(pk=pk) for pk in self.choices_picked]
