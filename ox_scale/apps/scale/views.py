from __future__ import unicode_literals

import random

from django.views.generic.detail import DetailView

from . import models


class RandomQuestion(DetailView):
    def get_object(self):
        qset = models.QuestionSet.objects.get(uuid=self.kwargs['uuid'])
        question = qset.questions.all()[random.randrange(0, qset.question_count)]
        question.impressions += 1
        question.save()
        return question
