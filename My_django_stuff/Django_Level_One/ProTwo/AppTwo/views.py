from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from AppTwo.models import Users

def index(request):
    return render(request, 'AppTwo/index.html')

def users(request):
    user_list = Users.objects.order_by('LastName')
    user_dict = {'users': user_list}
    return render(request, 'AppTwo/users.html', context=user_dict)
