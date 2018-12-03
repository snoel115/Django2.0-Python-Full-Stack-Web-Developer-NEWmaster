from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.\
from first_app.models import AccessRecord, Topic, Webpage

def index(request):
    # return HttpResponse("Hello word!")
    #note insert_me is a Django tag found in the template index.html
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record':webpage_list}
    return render(request, 'first_app/index.html', context=date_dict)
