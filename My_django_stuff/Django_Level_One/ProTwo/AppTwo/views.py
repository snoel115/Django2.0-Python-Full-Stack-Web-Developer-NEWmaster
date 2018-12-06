from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# from AppTwo.models import User
from AppTwo.forms import NewUserForm

def index(request):
    return render(request, 'AppTwo/index.html')

def users(request):
    # user_list = User.objects.order_by('LastName')
    # user_dict = {'users': user_list}
    # return render(request, 'AppTwo/user.html', context=user_dict)
    f = NewUserForm()
    if request.method == 'POST':
        f = NewUserForm(request.POST)

        if f.is_valid():
            f.save(commit=True)
            return index(request)
        else:
            print('ERROR FOR IS INVALID')

    return render(request, 'AppTwo/users.html', {'form': f})
