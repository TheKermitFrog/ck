from django.db import models

class songs(models.Model):
    title = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)
    album = models.CharField(max_length = 100)
    release_year = models.IntegerField()
    artist_genres = models.TextField(blank=True)
    added_at = models.DateField()
    added_by = models.CharField(max_length = 20)
    song_id = models.CharField(max_length = 100)
    danceability = models.DecimalField(max_digits=5, decimal_places=3)
    energy = models.DecimalField(max_digits=5, decimal_places=3)
    speechiness = models.DecimalField(max_digits=5, decimal_places=3)
    acousticness = models.DecimalField(max_digits=5, decimal_places=3)
    instrumentalness = models.DecimalField(max_digits=5, decimal_places=3)
    valence = models.DecimalField(max_digits=5, decimal_places=3)
