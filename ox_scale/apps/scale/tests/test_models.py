from django.test import TestCase

from ..factories import (QuestionSetFactory, ChoiceFactory, QuestionFactory,
    ResponseFactory, )


class QuestionSetTest(TestCase):
    def test_it_works(self):
        QuestionSetFactory()


class ChoiceTest(TestCase):
    def test_it_works(self):
        ChoiceFactory()


class QuestionTest(TestCase):
    def test_it_works(self):
        QuestionFactory()


class ResponseTest(TestCase):
    def test_choices_trivial_case(self):
        response = ResponseFactory()
        self.assertFalse(response.choices)
