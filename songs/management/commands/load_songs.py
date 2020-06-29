from csv import DictReader
import datetime
import os
import sys
from django.core.management import BaseCommand
from songs.models import songs
from pytz import UTC

RELEASEYEAR_FORMAT = '%Y'
DATE_FORMAT = '%Y-%m-%d'

ALREDY_LOADED_ERROR_MESSAGE = """
Data already loaded"""


class Command(BaseCommand):
    stealth_options = ("interactive",)
    # Show this when the user types help
    help = "Loads data from test_data.csv into songs model"

    def handle(self, *args, **options):
        os.chdir(sys.path[0])
        exists = os.path.exists('./songs.csv')

        if exists:
            print("Loading songs data")
            for row in DictReader(open('./songs.csv')):
                song = songs()
                song.title = row['Song Title']
                song.artist = row['Artist']
                song.album = row['Album']
                song.release_year = row['Release Date']
                song.artist_genres = row['Genres(Artist)']
                raw_added_date = row['Added at']
                added_date =  UTC.localize(
                    datetime.datetime.strptime(raw_added_date, DATE_FORMAT))
                song.added_at = added_date
                song.added_by = row['Added by']
                song.song_id = row['song_id']
                song.danceability = row['danceability']
                song.energy = row['energy']
                song.speechiness = row['speechiness']
                song.acousticness = row['acousticness']
                song.instrumentalness = row['instrumentalness']
                song.valence = row['valence']
                song.save()

            print(f'Loading Complete. Cronjob ends at {datetime.datetime.now()}')
            print()
            return

        else:
            print(f'Nothing to update, cronjob ends at {datetime.datetime.now()}')
            print()
            return
