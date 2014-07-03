import os

from django.core.files import File
from django.test import TestCase

from ..forms import DatasetFileImportForm


BASE_DIR = os.path.dirname(__file__)


class DatasetFileImportFormTest(TestCase):
    def test_clean_input_file_processes_file_to_rows(self):
        data = {
            'name': 'some name',
        }
        files = {
            'input_file': File(open(
                os.path.join(BASE_DIR, '..', 'fixtures', 'test_dataset.csv')
            )),
        }
        form = DatasetFileImportForm(data=data, files=files)
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.cleaned_data['input_file']), 3)
