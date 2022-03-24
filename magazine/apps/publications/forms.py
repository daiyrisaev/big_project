from django import forms

from apps.publications.models import Publication


class UserMailForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()


class MyPublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('title', 'description', 'poster')
