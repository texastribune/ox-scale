from django.test import TestCase

from ..factories import DatapointFactory


class DatapointTest(TestCase):
    def test_it_works(self):
        DatapointFactory()
