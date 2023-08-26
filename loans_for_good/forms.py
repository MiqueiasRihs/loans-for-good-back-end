from django import forms
from .models import UserFormConfiguration

from .utils import FIELD_OPTIONS

class UserFormConfigurationForm(forms.ModelForm):
    class Meta:
        model = UserFormConfiguration
        fields = ['field_settings']

    field_settings = forms.MultipleChoiceField(
        choices=FIELD_OPTIONS,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
