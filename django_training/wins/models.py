from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    song = models.CharField(max_length=50)
    release_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'


class Wins(models.Model):
    song = models.ForeignKey(Album, on_delete=models.CASCADE)
    date_of_winning = models.DateField()
    music_show = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Win'
        verbose_name_plural = 'Wins'
