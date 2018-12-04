#snoel new file =======================================================
from django import forms
from django.core import validators

# snoel individual field validator
def checkForZ(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('The Name field must start with a Z')

class FormName(forms.Form):
    # snoel - to use with a indivitual field validator
    name = forms.CharField(validators=[checkForZ])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    # By using Django to help us, we only need to do by importing the Django Validator
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

#======================================================================
