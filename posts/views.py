from django.shortcuts import render


# Create your views here.
def posts(request):
    return render(request, 'post/posts.html')


def postid(request, pk):
    pass
