from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models import Sum, Avg
# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @property 
    def artist_avg(self):
        queryset = self.song_set.all().filter(rating__gt=0).aggregate(Avg('rating'))
        return int(queryset['rating__avg'])
   


class Song(models.Model):
    artists = models.ManyToManyField(Artist)
    title = models.CharField(max_length=255)
    date = models.DateField(blank = True, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)], default=0)

    def __str__(self):
        return self.title



   
