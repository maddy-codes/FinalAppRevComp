from django import forms

class NameFileForm(forms.Form):
    name = forms.CharField(max_length=200)
    file = forms.FileField()

class ExcelDateForm(forms.Form):
    end_date = forms.CharField(max_length=200)
    excel_sheet = forms.FileField()
    