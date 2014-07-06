from django.views.generic import View

from . import models
from .forms import DatasetFileImportForm


class DatasetCreateFromFile(View):
    def post(self, request):
        form = DatasetFileImportForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            models.Dataset.objects.create(
                # TODO
                # owner=request.user,
                name=form.cleaned_data['name'],
            )

    def get(self, request):
        pass
