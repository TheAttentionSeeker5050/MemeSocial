# from unicodedata import category
from .models import Group
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):
    
    # group = GroupSerializer(many=False)
    
    class Meta:
        model = Group
        fields = ['pk', "group_name", "followers_number"]