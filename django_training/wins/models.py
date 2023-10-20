from django.db import models
from django.utils.text import slugify


class Artist(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, default='male')
    slug = models.SlugField(default='default-slug')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'
        db_table = 'artist'


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
        db_table = 'album'


class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'
        db_table = 'song'


class MusicShow(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'MusicShow'
        verbose_name_plural = 'MusicShows'
        db_table = 'music_show'


class Win(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    date_of_winning = models.DateField()
    music_show = models.ForeignKey(MusicShow, on_delete=models.CASCADE)
    youtube_link = models.CharField(max_length=200, default='https://www.youtube.com/')

    class Meta:
        verbose_name = 'Win'
        verbose_name_plural = 'Wins'
        db_table = 'win'
