from django.urls import reverse, include, path
from rest_framework import status
from rest_framework.test import APITestCase

from posts.models import Post
from django.contrib.auth.models import User
from groups.models import Group

import datetime

# from django.core.files import File

# imports to make an image file
import os
import io

from PIL import Image

class APIPostTest(APITestCase):
    
    def generate_photo_file(self):
        """We generate a dummy image file"""
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'meme.png'
        file.seek(0)
        return file
    

    def test_create_post(self):
        """
            Ensure we can create a new post object with api calls
        """

        # we need to first create a dummmy group and user objects, as it is a foreign key in post
        User.objects.create(username="nicolas", password="123456")
        Group.objects.create(group_name="General", followers_number=100)

        image_file = self.generate_photo_file()

        data = {
            "posted_by": "nicolas",
            "title": "Power dog safe feeling.",
            "group": "General",
            "content": "Man fast however industry buy score general behind staff design.",
            "meme": image_file,
            "date_posted": "2022-03-09T19:21:44Z"
        }

        url = reverse("rest_api:posts-list")
        response = self.client.post(url, data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
    
    

