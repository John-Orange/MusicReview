from django.db import models
from  django.contrib.auth.models import User

# Create your models here.

class MusicType(models.Model):
    typename=models.CharField(max_length=225)
    typedescription=models.CharField(max_length=225)

    def __str__(self):
        return self.typename
    
    class Meta:
        db_table='musictype'

class Author(models.Model):
    name=models.CharField(max_length=225)
    DOB=models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        db_table='author'

class Song(models.Model):
    songname=models.CharField(max_length=225)
    songtype=models.ForeignKey(MusicType, on_delete=models.CASCADE)
    authorname=models.ForeignKey(Author, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    releaseDate=models.DateField()
    YoutubeURL=models.URLField()
    songdescription=models.TextField()

    def __str__(self):
        return self.songname

    class Meta:
        db_table='song'