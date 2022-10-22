from django.views import generic
# from .models import Post
from django.http import HttpResponse


# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")