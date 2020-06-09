from django.shortcuts import render

# Create your views here.
def gallery(request):
    return render(request,'/home/stamatis/Desktop/stamtravelblog-project/gallery/templates/gallery.html')
