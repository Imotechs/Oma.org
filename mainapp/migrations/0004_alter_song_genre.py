# Generated by Django 4.0.1 on 2022-06-07 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_song_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.genre'),
        ),
    ]
