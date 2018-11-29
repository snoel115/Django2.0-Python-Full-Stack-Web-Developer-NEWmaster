from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<em>My Second Application ... Oh Canada</em>")

def help(request):
    my_dict = {'insert_help_here': "HELP PAGE"}
    return render(request, 'AppTwo/help.html', context=my_dict)
