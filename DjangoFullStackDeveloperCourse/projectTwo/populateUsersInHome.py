import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','projectTwo.settings')

import django
django.setup()

import random
from home.models import Users
from faker import Faker

def genUser():
    fakegen = Faker()
    fake_email = fakegen.email()
    fullName = ""
    tmpUser = Users.objects.get_or_create(email=fake_email)
    if tmpUser[1]:
        tmpUser=tmpUser[0]
        fullName = fakegen.name()
        fullName = fullName.split(' ')
        print(fullName)
        tmpUser.lastname = fullName.pop()
        print(tmpUser.lastname)
        tmpUser.firstName = ""
        for string in fullName:
            tmpUser.firstName+=string
        print(tmpUser.firstName)
        tmpUser.save()

def populate(N=5):
    for n in range(N):
        genUser()
if __name__ == "__main__":
    print("Populating..")
    populate(1000)
    print("done!")
