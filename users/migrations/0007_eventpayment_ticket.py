# Generated by Django 4.0.1 on 2022-07-05 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_withdrowal_account_name_withdrowal_account_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpayment',
            name='ticket',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
