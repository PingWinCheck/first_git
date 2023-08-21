from django import forms
from django.core.exceptions import ValidationError

from .models import *


class BackFilterForm(forms.Form):
    title = forms.CharField(max_length=50, required=False)
    name = forms.IntegerField(required=False)
    kek = forms.BooleanField(required=False)


class ModelForm(forms.ModelForm):
    """Forms to add telephone in db"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['firm'].empty_label = 'Фирма не выбрана'
    class Meta:
        model = Mobile
        fields = ['firm', 'name', 'price', 'slug']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 4:
            raise ValidationError('Длина больше 4')

        # return name

# class DelMobile(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # CHOICES = (('op1', 'ope1'),('op2', 'ope2'))
#         a = Mobile.objects.all()
#         CHOICES = []
#         for i in a:
#             CHOICES.append((i, i))
#         print(CHOICES)
#         self.fields['name'].widget = forms.Select(choices=CHOICES)
#     class Meta:
#         model = Mobile
#         fields = ['name',]

