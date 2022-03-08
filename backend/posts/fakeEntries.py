# import faker
from faker import Faker

#import db
from .models import Post
from users.models import Profile
from groups.models import Group

fake = Faker()

for i in range(0-1000):
    