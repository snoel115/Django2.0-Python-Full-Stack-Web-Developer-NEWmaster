#snoel new file =======================================================
from django import forms
from django.core import validators

# snoel individual field validator
def strMustStartWithTheLetterZ(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('The Name field must start with a Z')

class FormName(forms.Form):
    # snoel - to use with a indivitual field validator
    name = forms.CharField(validators=[strMustStartWithTheLetterZ])

    #create a second email field to double-check ... many site request the user to type his email address twice
    # note that this step is not necessary
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')

    text = forms.CharField(widget=forms.Textarea)

    # By using Django to help us, we only need to do by importing the Django Validator
    # this is an invisible field (nicked eye) ... but as a bot populate forms in usign the html directly, the bot will entered
    # information in this field. We expect this to be always empty. So, if there is something, a bot pushes information
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    #snoel - this will validate the entire form at once
    # otherwise, you can validate each fied at the time, but this will be anoying for the end user
    def clean(self):
        all_clean_data = super().clean()
        #check if the email is valid
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Make sure you entered a valid email')
#======================================================================
