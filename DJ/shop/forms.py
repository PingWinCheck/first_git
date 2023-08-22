from django import forms
from .models import *


class RegForm(forms.Form):
    title = forms.CharField(max_length=5, label='Логин')
    check_box = forms.BooleanField(label='чек бокс')
    name = forms.ModelChoiceField(queryset=Mobile.objects.all(), empty_label='Пусто')
    cal = forms.CharField(max_length=255, widget=forms.SelectDateWidget)

