#snoel - create fake data for the first_app models ========================
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproject.settings')

import django
django.setup()

#FAKE POP Script

import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topic = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_Topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topic))[0]
    t.save()
    return t


def populate(N=5):

    for entry in range(N):
        #get topic or entry
        top = add_Topic()

        #create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        #create a fake access record for that Webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('populate complete ')





#=========================================================================
