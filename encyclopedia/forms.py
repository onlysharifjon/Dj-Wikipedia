from django import forms
from .models import Page


class CreatePageForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(label='Description (only markdown)',
                                  widget=forms.Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Page
        fields = ['title', 'description']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }


class EditPageForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(label='Description (only markdown)',
                                  widget=forms.Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Page
        fields = ['title', 'description']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }
