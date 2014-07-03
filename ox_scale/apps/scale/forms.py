from django import forms


class DatasetFileImportForm(forms.Form):
    # sort of a model form for `Dataset`
    name = forms.CharField(max_length=255)
    input_file = forms.FileField()

    def clean_input_file(self):
        """Turn the input file into a list of `Datapoint` data."""
        data = self.cleaned_data['input_file']
        # TODO process as CSV
        return data.readlines()
