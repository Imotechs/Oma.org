# Generated by Django 4.0.1 on 2022-06-09 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_album_event_rename_image_song_song_logo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
