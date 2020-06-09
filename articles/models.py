from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    pub_date=models.DateField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to="media/")
    icon = models.ImageField(upload_to="media/")
