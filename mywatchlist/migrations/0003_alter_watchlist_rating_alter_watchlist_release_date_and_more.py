# Generated by Django 4.1 on 2022-09-21 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0002_watchlist_delete_mywatchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='release_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='watched',
            field=models.BooleanField(),
        ),
    ]
