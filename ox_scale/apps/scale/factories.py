from __future__ import unicode_literals

import factory

from . import models


class QuestionSetFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.QuestionSet
    name = factory.Sequence(lambda i: 'QuestionSet {}'.format(i))


class ChoiceFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Choice
    set = factory.SubFactory(QuestionSetFactory)
    choice = factory.Sequence(lambda i: 'Choice {}'.format(i))


class QuestionFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Question
    set = factory.SubFactory(QuestionSetFactory)
    question = factory.Sequence(lambda i: 'Question {}'.format(i))


class ResponseFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Response
    question = factory.SubFactory(QuestionFactory)
