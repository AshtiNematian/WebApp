from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from taggit.models import Tag
from Blog.serializer import PostSerializer
from django.shortcuts import get_object_or_404
from Blog.models import Post
from rest_framework import filters, generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class PostTagsViews(generics.GenericAPIView):
    serializer_class = PostSerializer

    def tagged(self, slug):
        tag = get_object_or_404(Tag, slug=slug)
        # Filter posts by tag name
        posts = Post.objects.filter(tags=tag)
        context = {
            'tag': tag,
            'posts': posts,

        }
        return render(self, context)


# Display Posts


class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class RetrieveDeletePost(GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Post Search


class PostListDetailfilter(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']


class CreatePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class EditPost(generics.UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
