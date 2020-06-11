from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
import articles.views
import destinations.views
import contact.views
import gallery.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/',articles.views.articles,name="articles"),
    path('',articles.views.home,name="home"),
    path('destinations/',destinations.views.destinations,name="destinations"),
    path('contact/', contact.views.contact,name="contact"),
    path('blog/',articles.views.blog,name="blog"),
    path('about/',articles.views.about,name="about"),
    path('gallery/',gallery.views.gallery,name="gallery"),






]  + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
