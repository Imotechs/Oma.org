# Generated by Django 4.0.1 on 2022-07-08 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_eventpayment_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=10000)),
                ('source', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/news/')),
                ('uploaded_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
