from rest_framework import serializers
from post.models import Post

#class PostSerializer(serializers.Serializer):
#    title = serializers.CharField(max_length=200)
#    content = serializers.CharField(max_length=200)

class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug'
    )
    #username = serializers.SerializerMethodField(method_name='username_new')
    username = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'username',
            'title',
            'content',
            'image',
            'url',
            'created',
            'modified_by'
        ]

    def get_username(self,obj):
        return str(obj.user.username)

    #def username_new(self,obj):
    #    return str(obj.user.username)

class PostUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]

    """
    def validate_title(self,value):
        if value == "cemaldak":
            raise serializers.ValidationError("Bu değer olmaz.")
        return value
    
    def validate(self,attrs):
        if attrs['title'] == "oguzhan":
            raise serializers.ValidationError("Olmaz.")
        return attrs
    """
    
