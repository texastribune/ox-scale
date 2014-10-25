from __future__ import unicode_literals

import random

from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView

from . import models


class RandomQuestion(DetailView):
    def get_object(self):
        qset = models.QuestionSet.objects.get(uuid=self.kwargs['uuid'])
        question = qset.questions.all()[random.randrange(0, qset.question_count)]
        question.impressions += 1
        question.save()
        return question


def question_response(request, uuid):
    """
    Store the user's response in the database.

    I'm not using a CBV because there nothing reusable about any of this logic.
    """
    if request.method != 'POST':
        return HttpResponseNotAllowed(('POST',))
    question = get_object_or_404(models.Question,
        pk=request.POST['question'], set__uuid=uuid)
    # Don't bother checking to see if these answers are valid for performance,
    # we can batch that later. TODO
    answer = ','.join(request.POST.getlist('response'))
    assert answer  # ma
    models.Response.objects.create(
        question=question,
        choices_picked=answer,
        meta={},  # TODO
    )

    # TODO render something
    return HttpResponse('ok')
