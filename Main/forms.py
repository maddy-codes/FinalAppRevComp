from django import forms

class NameFileForm(forms.Form):
    name = forms.CharField(max_length=200)
    file = forms.FileField()