# Generated by Django 4.1 on 2022-09-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0005_alter_watchlist_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='release_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='watched',
            field=models.CharField(max_length=100),
        ),
    ]
