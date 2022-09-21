from django.db import models

class WatchList(models.Model):
    watched = models.CharField(max_length=100)
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()  
    review = models.TextField()