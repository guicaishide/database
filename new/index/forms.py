from .models import *
from django import forms

class AccountForm(forms.ModelForm):
    class Meta:
        model=AccountModel
        fields="__all__"

class LeftForm(forms.ModelForm):
    class Meta:
        model=LeftModel
        fields="__all__"

class LeftMiddleForm(forms.ModelForm):
    class Meta:
        model=LeftMiddleModel
        fields="__all__"

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model=ArticleModel
        fields="__all__"