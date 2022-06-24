# Generated by Django 4.0.1 on 2022-06-09 08:12

from django.db import migrations, models
import django.db.models.deletion
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_song_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=30)),
                ('album_logo', models.ImageField(upload_to=mainapp.models.user_directory_path)),
                ('uploaded_on', models.DateTimeField(auto_now=True)),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.artist')),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('event_date', models.CharField(max_length=30)),
                ('event_time', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=50)),
                ('uploaded_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='song',
            old_name='image',
            new_name='song_logo',
        ),
        migrations.AddField(
            model_name='song',
            name='uploaded_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(upload_to='media/songs'),
        ),
        migrations.CreateModel(
            name='ArtistSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('song_logo', models.ImageField(blank=True, null=True, upload_to=mainapp.models.uploaded_path)),
                ('audio_file', models.FileField(blank=True, null=True, upload_to=mainapp.models.user_directory_path_song)),
                ('uploaded_on', models.DateTimeField(auto_now=True)),
                ('album_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.album')),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.artist')),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.genre')),
            ],
        ),
    ]