# Generated by Django 4.0.1 on 2022-07-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_account_withdrowal_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrowal',
            name='account_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='withdrowal',
            name='account_number',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='withdrowal',
            name='account_type',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='withdrowal',
            name='bank',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='withdrowal',
            name='amount',
            field=models.FloatField(default=0, verbose_name='Amount to withdraw'),
        ),
    ]