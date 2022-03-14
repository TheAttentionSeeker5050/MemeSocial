from django.test import TestCase

from posts.models import Post
from django.contrib.auth.models import User
from groups.models import Group

class PostModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """we create an element for the model"""

        # we need to first create a dummmy group and user objects, as it is a foreign key in post

        Group.objects.create(group_name="General", followers_number=100)
        User.objects.create(username="nicolas", password="123456")
        Post.objects.create(posted_by=User.objects.first(), title="title54654 1652763r4 -.-.,-,-.-. +#$", group=Group.objects.get(), content="sjkdjsdn sdkjfhnekrjfgvnd kjsndfvjkhd  jfwkehrjfwe em,kwerjgre ekfjwejkhr wekfwjihf", meme="/img/meme (55).jpg", date_posted="2022-03-09T19:21:44Z")
    
    def test_string_method(self):
        """We get the default string when calling a table element and make sure 
        it is equal to an expected string"""
        post = Post.objects.get()
        expected_string = f"{post.title}"
        self.assertEqual(str(post), expected_string)
    
    def test_get_absolute_url(self):
        """we test the url"""
        post = Post.objects.get()
        self.assertEqual(post.get_absolute_url(), "/posts/2/")
