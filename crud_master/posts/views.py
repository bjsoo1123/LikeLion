from django.shortcuts import render

def create(request):
    form = PostForm()
    return render(request, 'posts/create.html')