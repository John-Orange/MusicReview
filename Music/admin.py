from django.contrib import admin
from .models import MusicType, Author, Song

# Register your models here.

admin.site.register(MusicType)
admin.site.register(Author)
admin.site.register(Song)
