# social/dwitter/forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Gweet 


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", )


class GweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True, 
        widget=forms.widgets.Textarea(attrs={
            "placeholder": "Gweet what's going on",
            "class": "textarea is-info is-medium",
        }
        ),
        label="",
        )

    class Meta:
        model = Gweet
        exclude = ("user",)
