# Generated by Django 4.0.1 on 2022-06-11 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0010_artist_date_joined_alter_artistsong_album_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
