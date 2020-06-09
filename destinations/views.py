from django.shortcuts import render

# Create your views here.
def destinations(request):
    return render(request,"destinations.html")
