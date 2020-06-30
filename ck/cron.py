from .Spotify_functions import CK_spotify
import os
import sys
import datetime
from django.core.management import call_command

def check_for_update():
    print(datetime.datetime.now())
    os.chdir(sys.path[0])
    client = CK_spotify()
    client.authorize()
    client.fetch_playlist_data()
    ids = client.get_songs_id()
    if len(ids) >= 100:
        print('Over 100 songs, transferring to archive')
        client.to_csv()
        client.transfer_songs()
        print()
    else:
        print(f'Total {len(ids)} songs, nothing executed.')
        print()
    return

def update():
    call_command('load_songs', verbosity=0, interactive=False)
    return

def remove_csv_data():
    os.chdir(sys.path[0])
    exists = os.path.exists('./songs.csv')
    if exists:
        print("File exists, removing...")
        os.remove('./songs.csv')
        print(f"Removal complete. Cronjob ends at {datetime.datetime.now()}")
        print()
        return
    else:
        print(f"File does not exist, Cronjob ends at {datetime.datetime.now()}")
        return
