from rest_framework.serializers import ModelSerializer,SerializerMethodField
from comment.models import Comment
from rest_framework import serializers
from django.contrib.auth.models import User
from post.models import Post

class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created','user']

    def validate(sellf,attrs):
        if(attrs['parent']):
            if(attrs["parent"].post != attrs["post"]):
                raise serializers.ValidationError("something went wrong")

        return attrs

"""
class CommentChildSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
"""

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)
        #fields = ('firsst_name','last_name')


class PostCommentSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','slug','id')

class CommentListSerializer(ModelSerializer):
    replies = SerializerMethodField()
    user = UserSerializer()
    post = PostCommentSerializer()
    class Meta:
        model = Comment
        fields = '__all__'
        #depth = 1 #bütün bilgileri getircek user ya da post

    def get_replies(self,obj):
        if obj.any_children:
            return CommentListSerializer(obj.children(), many=True).data


class CommentDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]
