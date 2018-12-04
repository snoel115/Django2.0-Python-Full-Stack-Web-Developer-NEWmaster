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
    #create a second email field to double-check
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)

    # By using Django to help us, we only need to do by importing the Django Validator
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    #snoel - this will validate the entire form at once
    def clean(self):
        all_clean_data = super().clean()
        #check if the email is valid
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Make sure you entered a valid email')
#======================================================================
