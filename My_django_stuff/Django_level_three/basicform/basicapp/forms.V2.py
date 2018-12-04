#snoel new file =======================================================
from django import forms
from django.core import validators

class FormName(forms.Form):
    # snoel - to use with a indivitual field validator
    # name = forms.CharField(validators=[checkForZ])
    name = forms.CharField()
    email = forms.EmailField()
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput)

    # snoel - hidden field for bot`
    # snoel create the clean_NameOfTheHiddenField used for the bot
    # this field is supposed to be always empty as a bot fill out a form_page
    # by using the html directly
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            # this field is supporsed to be empty as it is invisible
            raise forms.ValidationError('GOTCHA BOT')

        return botcatcher

#======================================================================
