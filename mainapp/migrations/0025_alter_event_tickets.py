# Generated by Django 4.0.1 on 2022-06-21 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_artist_account_alter_artist_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='tickets',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
