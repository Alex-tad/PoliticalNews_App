# news/youtube_fetcher.py

import requests
from .models import YouTubeVideo
from django.utils.dateparse import parse_datetime

API_KEY = 'AIzaSyBpPTFC9p6clZazc8NgSpsWbP_JCO4aat4'  # Replace this with your real API key

CHANNEL_IDS = [
    'UC0EXRgDZOfs7z4M3xBCKhpw',  # Ethio 360
    'UCcs9pBjQy8tgqQdjSnuOy4g',  # ESAT
    'UCckz6n8QccTd6K_xdwKqa0A',  # AFP
    'UCbbS1GE942k3UVqpLklyhIA',  # DW
    'UC25EuGAePOPvPrUA5cmu3dQ',  # African News
    'UChqUTb7kYRX8-iaN3XFrSQ',   # Reuters
    'UCpEKp4y4xXwIiF9E3zKJESw',  # Zehabesha
    'UC16niRr50-MSBwiO3YDb3RA',  # BBC News
    'UCY2_DU9u0qvz6l47o28L2JA',  # Mereja
    'UCDXU7RuIQc0xRKJyP0ZTZaQ',  # Roha Media
    'UCtD355G8T_f0e3dXwWiv3DA',  # NBC Amhara
    'UCQwdCM4dBMgxPh0UZa8PIow',  # Wazema Radio
    'UCwVgkpOa9qZNOtz_hDhnHeg',  # Reporter Ethiopia
    'UCSjaw-eGJSkvcXHyTpQyT1Q',  # Ethiopian News Agency
    'UCOhrz3uRCOHmK6ueUstw7_Q',  # EBC
    'UCXUFyN9Ys5tiIHgJFQKRJvA',  # Ethio Forum
    'UC6qleAb8V7CkqhAwlxoWozg',  # Hibir Radio
    'UCelbYFUaQW3eb9sg3004ZGw',  # Ethio News
    'UCCJbY4YdJIUk7Lygrkg5IRA',  # EMS
    'UCEwesckppGKcJoEsd67JowA',  # Hagere TV
    'UC3-RNH75BEZslJLEoIAxa2A',  # DW Amharic
    'UCeuqPLAm0q2AV0Sg8ju3wIw',  # Maede Zena
    'UCPVr1rrKl8pXVFi-rrqzS1g',  # Reyot Media
    'UC52X5wxOL_s5yw0dQk7NtgA',  # Associated Press
    'UCKZGcrxRAhdUi58Mdr565mw',  # African Diaspora News
    'UCd43apgU3-ypkarb2YYbBIQ',  # Anchor Media
    'UC0LjMR-ZJ2lUBt17zVNHfZw',  # Andafta
    'UC_m5g0TeOmYTPb535BLWd9Q',  # Ethio Focus
    'UCwMHDoJO6cHO6LN1BItFsPQ',  # Andafta 2
]

def fetch_youtube_videos():
    for channel_id in CHANNEL_IDS:
        url = (
            f'https://www.googleapis.com/youtube/v3/search'
            f'?key={API_KEY}'
            f'&channelId={channel_id}'
            f'&part=snippet'
            f'&order=date'
            f'&maxResults=5'
        )
        response = requests.get(url)
        data = response.json()

        for item in data.get('items', []):
            if item['id'].get('kind') == 'youtube#video':
                video_id = item['id']['videoId']
                snippet = item['snippet']
                published_at = parse_datetime(snippet['publishedAt'])

                YouTubeVideo.objects.get_or_create(
                    video_id=video_id,
                    defaults={
                        'title': snippet['title'],
                        'description': snippet['description'],
                        'channel_title': snippet['channelTitle'],
                        'published_at': published_at,
                        'thumbnail_url': snippet['thumbnails']['high']['url'],
                    }
                )
