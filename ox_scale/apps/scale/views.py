from django.views.generic import View

from . import models
from .forms import DatasetFileImportForm


class DatasetCreateFromFile(View):
    def post(self, request):
        form = DatasetFileImportForm(data=request.POST)
        if form.is_valid():
            models.Dataset.create(
                # TODO
                # owner=request.user,
                name=form.cleaned_data['name'],
            )
