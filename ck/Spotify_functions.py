import spotipy
import spotipy.util as util
import os
import pandas as pd
import math
from .credentials import credentials

class CK_spotify:
    def __init__(self):
        self.username = credentials['username']
        self.scope = credentials['scope']
        self.client_id = credentials['client_id']
        self.client_secret = credentials['client_secret']
        self.redirect_uri = credentials['redirect_uri']
        self.playlist_id = '6LmP4jkYHQzbjA2ltohL04'
        self.archive_id = '43E3cju7xCSKxoip9QWV7i'
        self.user_dict = {
            "spotify:user:ct9h0dxd6nw3y0i0jwbeql8q7" : "Darren",
            "spotify:user:11120487705" : "Kuan",
            "spotify:user:peter1234603" : "Yuting",
            "spotify:user:jppxvr2b5cplrp9bckbw5boqj" : "Brian",
            "spotify:user:jaysonwu1995" : "JaysonWu",
            "spotify:user:92l8q1k3guyi69mbcos3lqyjj" : "Hung-Chen Yu",
            "spotify:user:11126832469" : "Ray Chang",
            "spotify:user:11127396160" : "Jun Yeah",
            "spotify:user:11100001859" : "Meng"
            }

    def authorize(self):
        token = util.prompt_for_user_token(self.username,
                                           self.scope,
                                           self.client_id,
                                           self.client_secret,
                                           self.redirect_uri)
        if token:
            print('Token generated')
            self.sp = spotipy.Spotify(auth=token)
            print('Initiated Spotipy API')
            return
        else:
            return (f"Can't get token for usename: {self.username}")

    def fetch_playlist_data(self):
        results = self.sp.playlist(self.playlist_id,
                                              fields=None, market=None,
                                              additional_types=('track', ))
        results = results['tracks']
        tracks = results['items']
        while results['next']:
            results = self.sp.next(results)
            tracks.extend(results['items'])
        self.playlist_data = tracks
        self.total_songs = len(tracks)
        print('Playlist data fetched')
        return

    def fetch_archive_data(self):
        results = self.sp.playlist(self.archive_id,
                                   fields=None, market=None,
                                   additional_types=('track', ))
        results = results['tracks']
        tracks = results['items']
        while results['next']:
            results = self.sp.next(results)
            tracks.extend(results['items'])
        self.archive_data = tracks
        self.total_songs_archived = len(tracks)
        print('Archive data fetched')
        return

    def to_csv(self, objective = 'playlist'):
        data = {
        "Song Title" : [],
        "Artist" : [],
        "Album" : [],
        "Release Date" : [],
        "Genres(Artist)" : [],
        "Added at" : [],
        "Added by" : [],
        'danceability' : [],
        'energy': [],
        'speechiness': [],
        'acousticness': [],
        'instrumentalness': [],
        'valence': [],
        'song_id' : [],
        }

        if objective == 'playlist':
            target = self.playlist_data
        elif objective == 'archive':
            target = self.archive_data

        for item in target:
            track = item['track']
            artist_id = track['artists'][0]['id']
            song_id = track['id']
            audio_features = self.sp.audio_features(song_id)
            data['Song Title'].append(track['name'])
            data['Artist'].append(track['artists'][0]['name'])
            data['Album'].append(track['album']['name'])
            data['Release Date'].append(track['album']['release_date'][:4])
            data['Genres(Artist)'].append(', '.join(self.sp.artist(artist_id)['genres']))
            data['Added at'].append(item['added_at'].split('T')[0])
            data['Added by'].append(self.user_dict[item['added_by']['uri']])
            data['danceability'].append(audio_features[0]['danceability'])
            data['energy'].append(audio_features[0]['energy'])
            data['speechiness'].append(audio_features[0]['speechiness'])
            data['acousticness'].append(audio_features[0]['acousticness'])
            data['instrumentalness'].append(audio_features[0]['instrumentalness'])
            data['valence'].append(audio_features[0]['valence'])
            data['song_id'].append(song_id)
        df = pd.DataFrame(data=data)
        df.to_csv('./songs.csv', index=False)
        print('Data saved to file.')
        return data

    def get_songs_id(self, objective = 'playlist'):
        if objective == 'playlist':
            target = self.playlist_data
        elif objective == 'archive':
            target = self.archive_data

        id_list = []
        for track in target:
            id_list.append(track['track']['id'])
        return id_list

    def add_songs_to_archive(self):
        id_list = self.get_songs_id()
        for i in range(math.ceil(len(id_list) / 100)):
            offset = 100 * i
            if(offset + 100 <= len(id_list)):
                print(f"Adding songs {offset + 1} to {offset + 100} to archive.")
                self.sp.user_playlist_add_tracks('ct9h0dxd6nw3y0i0jwbeql8q7', self.archive_id, id_list[offset:offset+99], position=None)
            else:
                print(f"Adding songs {offset + 1} to {len(id_list)} to archive.")
                self.sp.user_playlist_add_tracks('ct9h0dxd6nw3y0i0jwbeql8q7', self.archive_id, id_list[offset:], position=None)
        print('All songs added to archive.')
        return

    def remove_songs_from_playlist(self):
        self.sp.user_playlist_replace_tracks('ct9h0dxd6nw3y0i0jwbeql8q7', self.playlist_id, [])
        print('All songs removed from playlist.')
        return

    def transfer_songs(self):
        self.add_songs_to_archive()
        self.remove_songs_from_playlist()
        print('Transfer complete')
        return
