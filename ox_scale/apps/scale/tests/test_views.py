from __future__ import unicode_literals

from django.test import TestCase

from ..factories import QuestionFactory
from ..models import Question
from ..views import RandomQuestion


class RandomQuestionTest(TestCase):
    def setUp(self):
        self.view = RandomQuestion()

    def test_get_object_works(self):
        # setup
        question = QuestionFactory(impressions=0)
        qset = question.set
        # `question_count` normally set when set is created
        qset.question_count = qset.questions.count()
        qset.save()
        self.view.kwargs = {'uuid': qset.uuid}

        obj = self.view.get_object()
        # assert question is returned since there's only one question
        self.assertEqual(obj, question)
        # clear model cache
        question = Question.objects.get(pk=question.pk)
        # assert impression was incremented
        self.assertEqual(question.impressions, 1)
