from rest_framework import serializers
from forum.models import Thread, Post


class ThreadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Thread
        fields = ('title', 'content_raw', 'order', 'hidden', 'closed')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('content_raw', 'hidden')
