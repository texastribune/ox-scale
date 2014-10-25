#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Load sample question set

This could also just be a fixture, but that would require some other work.
"""

import os.path

from ox_scale.apps.scale.models import QuestionSet
from ox_scale.apps.scale.utils import import_from_csv


BASE_DIR = os.path.dirname(__file__)


def main():
    import django; django.setup()  # XXX Django 1.7 weirdness

    obj = QuestionSet.objects.create(
        name='Sample questions',
    )
    path = os.path.join(BASE_DIR, '..', 'apps', 'scale', 'fixtures', 'sample_questions.csv')
    csv_file = open(path, 'rb')
    import_from_csv(obj, csv_file)
    obj.question_count = obj.questions.count()
    obj.save()


if __name__ == '__main__':
    main()
