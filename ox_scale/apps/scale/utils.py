from __future__ import unicode_literals

import csv
import codecs

from .models import Choice, Question


class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")


class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self


def import_from_csv(questionset, fh):
    reader = UnicodeReader(fh)
    for row in reader:
        assert len(row) > 1
        question = Question.objects.create(
            set=questionset,
            question=row[0],
        )
        for value in row[1:]:
            if value is '':
                # don't create empty choices
                continue
            choice, __ = Choice.objects.get_or_create(
                set=questionset, choice=value)
            question.choices.add(choice)
