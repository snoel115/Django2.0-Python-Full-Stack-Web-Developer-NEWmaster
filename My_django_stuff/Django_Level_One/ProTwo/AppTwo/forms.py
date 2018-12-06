# snoel - create this forms.py to hold the forms for this project ===================
from django import forms
from AppTwo.models import Users

# snoel here we use forms.ModelForm instead of forms.form as we want this to be connected
# directly to the DB
class NewUserForm(forms.ModelForm):
    class Meta():
        # here User is the model and not the form or the view
        model = Users
        # snoel - the "__all__" import all fields defined in the model
        fields = '__all__'

# ===================================================================================
