from lib2to3.refactor import MultiprocessRefactoringTool
from unicodedata import name
from django.test import TestCase
import datetime
from datetime import date
from django.contrib.auth.models import User
from .models import MusicType, Author, Song
from .forms import MTForm, AuthorForm, SongForm
from django.urls import reverse_lazy, reverse

# Create your tests here.

class MTTest(TestCase):
    def setUp(self):
        self.type = MusicType(typename='pop')

    def test_MTstring(self):
        self.assertEqual(str(self.type),'pop')

    def test_tablename(self):
        self.assertEqual(str(MusicType._meta.db_table), 'musictype')

class AuthorTest(TestCase):
    def setup(self):
        self.type = Author(name='Ed Sheeran')

    def test_Astring(self):
        self.assertEqual(str(self.type), 'ED Sheeran')

    def test_Astring(self):
        self.assertEqual(str(Author._meta.db_table),'author')

class SongTest(TestCase):
    def setUp(self):
        self.type=MusicType(typename='pop')
        self.author=Author(name='Ed Sheeran')
        self.user = User(username='user1')

        self.song1=Song(
            songname='Shape of you',
            songtype=self.type,
            authorname=self.author,
            user=self.user,
            songdescription='A Song',
            YoutubeURL='https://www.youtube.com/watch?v=JGwWNGJdvx8&list=PLMC9KNkIncKtGvr2kFRuXBVmBev6cAJ2u',
            releaseDate=date(2017,1,30),
        )

    def test_string(self):
        self.assertEqual(str(self.song1),'Shape of you')


class NewSongForm(TestCase):
    def test_SongForm(self):
        data = {
            'songname':'Fly me to the moon',
            'songtype':'jazz',
            'authorname':'Frank Sinatra',
            'user':'huang',
            'releaseDate':'1964-01-01',
            'YoutubeUrl':'https://www.youtube.com/watch?v=CFlMy48ui9s',
            'songdescription':'Jazz song',
             }
        
        form=SongForm(data)
        self.assertTrue(form.is_valid)

class New_Song_Authentication_Test(TestCase):
    def setUp(self):

        
        self.test_user=User.objects.create_user(username='user2', password='1029qpwo')
        self.type=MusicType.objects.create(typename='Rap')
        self.author=Author.objects.create(name='Test',DOB=datetime.date(2000,1,1))

        self.song=Song.objects.create(songname= 'Alright', 
        songtype=self.type, 
        authorname=self.author,
        user=self.test_user,
        releaseDate=datetime.date(2020,1,1), 
        YoutubeURL='https://store.google.com/', 
        songdescription= 'Testing' )

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newSong'))
        self.assertRedirects(response, '/accounts/login/?next=/Music/newSong/')