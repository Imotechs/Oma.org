# Generated by Django 4.0.1 on 2022-06-09 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_album_album_logo_alter_album_album_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='album_logo',
            field=models.ImageField(default='media/default.PNG', upload_to='media/Artist_profiles/'),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.ImageField(default='media/default.PNG', upload_to='media/Album_logo/'),
        ),
    ]
