# Generated by Django 4.0.1 on 2022-06-24 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0028_remove_artist_followers_alter_album_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='cancel',
            field=models.BooleanField(default=False),
        ),
    ]
