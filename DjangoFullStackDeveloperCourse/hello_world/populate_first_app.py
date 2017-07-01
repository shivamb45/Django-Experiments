#faking the data in databases

#setting the django env and settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import Topic,AccessRecord,Webpage
from faker import Faker

fakegen = Faker()
topics = ['Games','News','Search','Technology','Other']

def add_topic():
    tmpT = Topic.objects.get_or_create(topic_name = random.choice(topics))[0]
    tmpT.save()
    return tmpT

def populate(N=5):
    for r in range(N):
        #get a topic
        print('.',end=' ')
        tmpT = add_topic()

        #create fake data for Webpage, AccessRecord
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #save fake data
        webPg = Webpage.objects.get_or_create(topic = tmpT,name=fake_name,url=fake_url)[0]
        webPg.save()

        #save AccessRecord
        acRd = AccessRecord.objects.get_or_create(name=webPg,date=fake_date)[0]
        acRd.save()
if __name__ == "__main__":
    print("Populating the DB . ",end='')
    populate(200)
    print("\n\nPopulating Completed... !")
