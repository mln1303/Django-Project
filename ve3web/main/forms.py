from django import forms
from .models import CSVFile

class CSVFileForm(forms.ModelForm):
    class Meta:
        model = CSVFile
        fields = ('file',)
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file.name.endswith('.csv'):
            raise forms.ValidationError("Only .csv files are allowed.")
        return file