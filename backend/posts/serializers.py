
# from unicodedata import category
from .models import Post, Comment, SubComment
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    
    # group = GroupSerializer(many=False)
    
    class Meta:
        model = Post
        fields = ['pk', 'posted_by', 'title', "group", "content", "meme", "date_posted"]
        
        

class CommentSerializer(serializers.ModelSerializer):
    
    # nested relationship
    parent = PostSerializer(many=False)
    class Meta:
        model = Comment
        fields = ['pk', 'posted_by', 'parent', "content", "date_posted"]
        
class SubCommentSerializer(serializers.ModelSerializer):
    
    
    parent = CommentSerializer(many=False)
    
    class Meta:
        model = SubComment
        fields = ['pk', 'posted_by', 'parent', "content", "date_posted"]


# # here we create the meme image serializer
# from versatileimagefield.serializers import VersatileImageFieldSerializer
# from .models import MemeImage

# class MemeSerializer(serializers.ModelSerializer):
    

#     class Meta:
#         model = MemeImage
#         fields = ['pk',  'image']