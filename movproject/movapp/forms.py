from django import forms
from .models import Mov


class movform(forms.ModelForm):
    class Meta:
        model = Mov
        fields = ['name', 'desc', 'desc', 'image']
