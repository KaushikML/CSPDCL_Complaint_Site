from django import forms

class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    bp=forms.IntegerField()
    email = forms.EmailField()
    date = forms.DateField()
    complaint =forms.CharField(max_length=80)
    explain=forms.CharField(max_length=400)
