from django.shortcuts import render
from django.utils import timezone
from .models import Post
# import matlab.engine

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # eng = matlab.engine.start_matlab()
    # tf = eng.isprime(37)
    # return render(request, 'blog/post_list.html', {'posts': posts, 'tf': tf})
    return render(request, 'blog/post_list.html', {'posts': posts})

