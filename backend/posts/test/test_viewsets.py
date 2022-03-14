from django.test import TestCase
from django.urls import reverse

# import the db models
from posts.models import Post
from django.contrib.auth.models import User
from groups.models import Group

from posts.views import PostAPIViewset

# the datetime object
import datetime

class PostListViewsetTest(TestCase):
    
    """We test that the api view works fine"""

    @classmethod
    def setUpTestData(cls):
        """We use this to make test data and push it to the db"""

        number_of_posts = 100

        # we will create a group and user instance, as the post models takes them as foreign key
        Group.objects.create(group_name="General", followers_number=100)
        User.objects.create(username="nicolas", password="123456")

        for post_id in range(1,number_of_posts+1):
            Post.objects.create(posted_by=User.objects.first(), title=f"title {post_id}", group=Group.objects.get(), content=(f"Content {post_id}"*10), meme="/img/meme (55).jpg", date_posted="2022-03-09T19:21:44Z")

    def test_url_exists(self):
        """
            We make sure that the posts url exists and we can get an http successful status
            response
        """

        response = self.client.get("/api/posts/")
        self.assertEqual(response.status_code, 200)
    

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("rest_api:posts-list"))
        self.assertEqual(response.status_code, 200)

    # def test_pagination_is_correct(self):
    #     response = self.client.get("/api/posts/")        
    #     self.assertEqual(response.status_code, 200)
            
        
    #     self.assertTrue("is_paginated" in response.context)
    #     self.assertTrue(response.context["is_paginated"] is True)
    #     # self.assertEqual(len(response.context["rest_api:posts-list"]), 5)