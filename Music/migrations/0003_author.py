# Generated by Django 4.0.3 on 2022-03-25 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0002_song_delete_musicname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('DOB', models.DateField()),
            ],
            options={
                'db_table': 'author',
            },
        ),
    ]
