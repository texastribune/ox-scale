from __future__ import unicode_literals

from django.http import Http404
from django.test import TestCase
from django.test.client import RequestFactory

from ..factories import QuestionFactory
from ..models import Question, Response
from ..views import RandomQuestion, question_response


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

        with self.assertNumQueries(3):
            obj = self.view.get_object()
        # assert question is returned since there's only one question
        self.assertEqual(obj, question)
        # clear model cache
        question = Question.objects.get(pk=question.pk)
        # assert impression was incremented
        self.assertEqual(question.impressions, 1)


class question_responseTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view = question_response

    def test_it_works(self):
        # setup
        question = QuestionFactory(impressions=0)
        uuid = question.set.uuid
        request = self.factory.post('/foo/', data={
            'question': question.pk,
            'response': 1,
        })
        # assert we started with no responses
        self.assertEqual(Response.objects.count(), 0)
        with self.assertNumQueries(2):
            response = self.view(request, uuid)
        self.assertEqual(response.status_code, 200)
        # assert there is now one response
        qresponse = Response.objects.all().get()
        self.assertEqual(qresponse.choices_picked, '1')

    def test_get_requests_are_rejected(self):
        request = self.factory.get('/foo/')
        response = self.view(request, 'bar')
        self.assertNotEqual(response.status_code, 200)

    def test_mismatched_questions_and_uuid_are_thrown_away(self):
        # setup
        question = QuestionFactory(impressions=0)
        request = self.factory.post('/foo/', data={
            'question': question.pk,
            'response': 1,
        })
        # assert we started with no responses
        self.assertEqual(Response.objects.count(), 0)
        with self.assertRaises(Http404):
            with self.assertNumQueries(1):
                self.view(request, 'baduuid')
        # assert there are still no responses
        self.assertEqual(Response.objects.count(), 0)
