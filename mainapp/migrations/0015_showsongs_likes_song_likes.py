# Generated by Django 4.0.1 on 2022-06-15 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_showsongs'),
    ]

    operations = [
        migrations.AddField(
            model_name='showsongs',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='song',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
