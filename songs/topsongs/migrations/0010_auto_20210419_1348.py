# Generated by Django 3.1.5 on 2021-04-19 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topsongs', '0009_playlist_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='date',
        ),
        migrations.AddField(
            model_name='playlist',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='playlist',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]