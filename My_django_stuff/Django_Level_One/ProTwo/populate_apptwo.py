#snoel - create fake data for the AppTwo models ========================
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

#FAKE POP Script

# import random
from AppTwo.models import Users
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):

        #create fake data for that entry
        fn = fakegen.first_name()
        ln = fakegen.last_name()
        email = fakegen.safe_email()

        #create a fake access record for that Webpage
        usr = Users.objects.get_or_create(FirstName=fn,
                                            LastName=ln,
                                            Email=email)[0]

if __name__ == '__main__':
    print('populating script')
    populate(50)
    print('populate complete ')





#=========================================================================
