# Generated by Django 5.0.6 on 2024-06-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='bp',
            field=models.IntegerField(null=True),
        ),
    ]