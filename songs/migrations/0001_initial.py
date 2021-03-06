# Generated by Django 3.0.3 on 2020-06-29 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('release_year', models.IntegerField()),
                ('artist_genres', models.TextField(blank=True)),
                ('added_at', models.DateField()),
                ('added_by', models.CharField(max_length=20)),
                ('song_id', models.CharField(max_length=100)),
                ('danceability', models.DecimalField(decimal_places=3, max_digits=5)),
                ('energy', models.DecimalField(decimal_places=3, max_digits=5)),
                ('speechiness', models.DecimalField(decimal_places=3, max_digits=5)),
                ('acousticness', models.DecimalField(decimal_places=3, max_digits=5)),
                ('instrumentalness', models.DecimalField(decimal_places=3, max_digits=5)),
                ('valence', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
    ]
