from django.db import models

# Create your models here.
class Gallery(models.Model):
    title=models.CharField(max_length=100)
    pub_date=models.DateField()
    image = models.ImageField(upload_to="media/")
    author=models.CharField(max_length=100)
