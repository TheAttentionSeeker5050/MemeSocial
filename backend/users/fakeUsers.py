from faker import Faker

#import db
from django.contrib.auth.models import User

fake = Faker()
Faker.seed(0)

for i in range(0,100):
    random_profile = fake.simple_profile()
    username = random_profile["username"]
    email = random_profile["mail"]
    password = random_profile["username"]

    username_entry = User.objects.create(username=username, password=password, email=email)
        
    username_entry.save()


admin_user = Profile.objects.create_user("nicocaste", password="202425NICo**", email="nicolas@castellano.com")
admin_user.is_superuser = True
admin_user.is_staff = True
admin_user.save()