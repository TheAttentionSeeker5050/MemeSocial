from django.shortcuts import render

# import the class based views and mixinns

from rest_framework import mixins
from rest_framework import generics

# import viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet, ModelViewSet

# import our model
from .models import Post, Comment, SubComment

# import serializer
from .serializers import PostSerializer, CommentSerializer, SubCommentSerializer

# import decorators
from rest_framework.decorators import action

# import pagination
from rest_framework.pagination import PageNumberPagination, CursorPagination
# Create your views here.


class PostAPIViewset(ModelViewSet):
    """This is the backend viewset and methods we will use for post to interact
    with the api"""
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # pagination_class = StandardResultsSetPagination
    
    @action(detail=True, methods=['post'])
    def upload_meme(request):
        try:
            file = request.data['file']
        except KeyError:
            raise ParseError('Request has no resource file attached')
        product = Post.objects.create(image=file)
    
    @action(detail=False)
    def get_list(self, request):
        pass
    @action(detail=True)
    def get_item(self, request, pk=None):
        pass
    @action(detail=True, methods=['post', 'delete'])
    def delete_item(self, request, pk=None):
        pass
    
    @action(detail=True, methods=['post'])
    def post_item(self, request, pk=None):
        pass
    @action(detail=True, methods=['put'])
    def update_item(self, request, pk=None):
        pass
    
    # def list(self, request):
    #     pass

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass
    
class CommentAPIViewset(PostAPIViewset):
    """This is the backend viewset for comments"""
    
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class SubCommentAPIViewset(PostAPIViewset):
    """This is the backend viewset for comments"""
    
    queryset = SubComment.objects.all()
    serializer_class = SubCommentSerializer
    
