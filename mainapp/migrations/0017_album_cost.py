# Generated by Django 4.0.1 on 2022-06-15 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_artist_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cost',
            field=models.FloatField(default=0),
        ),
    ]
