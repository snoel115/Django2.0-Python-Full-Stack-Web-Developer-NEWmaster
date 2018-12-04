from django.shortcuts import render

# Create your views here.
#snoel =================================
from . import forms

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

    if form.is_valid():
        #do something
        print('Validation success !!')
        print('name ' + form.cleaned_data['name'])
        print('emali ' + form.cleaned_data['email'])
        print('text ' + form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', {'form': form})
#=======================================
