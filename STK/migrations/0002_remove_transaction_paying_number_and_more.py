# Generated by Django 5.1.6 on 2025-02-09 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STK', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='paying_number',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='receiving_number',
        ),
        migrations.AddField(
            model_name='transaction',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
