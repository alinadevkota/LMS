from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from forum.models import Thread, Post
from forum.serializers import ThreadSerializer, PostSerializer


class SessionAuthenticationExemptCSRF(SessionAuthentication):

    def enforce_csrf(self, request):
        return


class ThreadApiView(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthenticationExemptCSRF,)
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer


class PostApiView(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthenticationExemptCSRF,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
