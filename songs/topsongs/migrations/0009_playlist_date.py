# Generated by Django 3.1.5 on 2021-04-19 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topsongs', '0008_auto_20210417_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
