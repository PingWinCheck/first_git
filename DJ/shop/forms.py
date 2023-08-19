from django import forms


class BackFilterForm(forms.Form):
    title = forms.CharField(max_length=50)
    name = forms.IntegerField()
    kek = forms.BooleanField()