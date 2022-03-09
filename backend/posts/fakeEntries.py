# import faker
from faker import Faker

#import db
from posts.models import Post
from django.contrib.auth.models import User
from groups.models import Group

import random

fake = Faker()
Faker.seed(0)


for i in range(0,1000):
    posted_by = User.objects.get(id=random.randrange(1, 101))
    title = fake.sentence(nb_words=4, variable_nb_words=True)
    group = Group.objects.get()
    content = fake.sentence(nb_words=8, variable_nb_words=True)
    date_posted = fake.date_time_this_month()
    # get random image from stored images
    meme = "/img/meme ({index}).jpg".format(index=random.randrange(1,101))

    post = Post.objects.create(posted_by=posted_by, title=title, group=group, content=content, date_posted=date_posted)

    post.save()