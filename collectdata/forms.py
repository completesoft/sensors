from .models import Datastring, DataSDM
from django import forms


class DatastringForm(forms.ModelForm):
    class Meta:
        model = Datastring
        fields = ['devid', 'temp']


class DataSDMForm(forms.ModelForm):
    class Meta:
        model = DataSDM
        fields = ['devid', 'val1', 'val2', 'val3']


