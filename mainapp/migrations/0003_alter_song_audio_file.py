# Generated by Django 4.0.1 on 2022-06-07 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_artist_user_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]