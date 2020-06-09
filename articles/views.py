from django.shortcuts import render
from .models import Article

# Create your views here.
def articles(request):
    articles=Article.objects
    return render(request,'articles/articles.html',{'articles':articles})


def home(request):
    return render(request,'articles/home.html')

def thankyou(request):
    return render(request,'articles/thankyou.html')

def blog(request):
    return render(request,'articles/blog.html')

def about(request):
    return render(request,'articles/about.html')
