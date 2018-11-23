from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    # return HttpResponse("<em>My Second Application ... Oh Canada</em>")
    my_dict = {'insert_help_here': "Hello I am from ProTwo/help.html!"}
    return render(request, 'AppTwo/help.html', context=my_dict)
