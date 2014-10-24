import os
import unittest

from django.test import TestCase, RequestFactory

from ..views import DatasetCreateFromFile
from .. import models


BASE_DIR = os.path.dirname(__file__)


@unittest.skip('TODO')
class DatasetCreateFromFileTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view = DatasetCreateFromFile()

    def test_post_creates_stuff(self):
        test_dataset = os.path.join(BASE_DIR, '..', 'fixtures',
            'test_dataset.csv')
        with open(test_dataset) as fp:
            request = self.factory.post('/foo/', {
                'name': 'bar',
                'input_file': fp,
            })
        response = self.view.post(request)
        print response
        self.assertTrue(models.Dataset.objects.filter(name='bar').exists())
