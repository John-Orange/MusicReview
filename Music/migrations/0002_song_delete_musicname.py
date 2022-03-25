# Generated by Django 4.0.3 on 2022-03-24 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songname', models.CharField(max_length=225)),
                ('releaseDate', models.DateField()),
                ('YoutubeURL', models.URLField()),
                ('songdescription', models.TextField()),
                ('songtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Music.musictype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'song',
            },
        ),
        migrations.DeleteModel(
            name='MusicName',
        ),
    ]