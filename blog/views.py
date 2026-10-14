from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog(request):
    return render(request, 'blog/blog.html')
def post(request,pk):
    return render(request, 'blog/post.html', {'pk': pk})
def home(request):
    first_name = 'John'
    last_name = 'Doe'
    my_name = f"{first_name} {last_name}"
    return render(request, 'blog/home.html',{'title': 'Home variable', 'my_name': my_name})