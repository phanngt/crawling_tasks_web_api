import re

rep_youtube_url = re.compile(
    r'(?:(?:youtu\.be/)|(?:youtube.com/watch\?v=))(.+)$')


def extract_youtube_id_from_url(y_url):
    rem = rep_youtube_url.findall(y_url)
    if not rem:
        return None
    return rem[0]
