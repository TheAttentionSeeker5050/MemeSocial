
from rest_framework.routers import DefaultRouter
from posts.views import PostAPIViewset

from django.urls import reverse, include, path
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

class APIPostURLTestCase(APITestCase, URLPatternsTestCase):
    router = DefaultRouter()
    router.register(r'posts', PostAPIViewset, basename='posts')
    urlpatterns = [
        path("api/", include(router.urls))
    ]
    def test_create_post(self):
        """
            We make sure we can get a correct url response when calling the post main url
        """

        url = reverse("posts-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        