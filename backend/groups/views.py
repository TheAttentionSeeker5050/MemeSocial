from django.shortcuts import render

# Create your views here.

# import viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet, ModelViewSet

# import our model
from .models import Group

# import serializer
from .serializers import GroupSerializer

# import decorators
from rest_framework.decorators import action

# Create your views here.


class GroupAPIViewset(ModelViewSet):
    """we get all posts no matter what is their group"""
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
    
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
    
