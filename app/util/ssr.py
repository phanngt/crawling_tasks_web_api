import os
import urllib.parse

from flask import send_from_directory
from requests import request

ssr_token = os.environ.get('SSR_TOKEN')
cache_html_path = os.environ.get('PRERENDER_DIR')


def encode_uri_component(url):
    return urllib.parse.quote(url.encode())


def is_bot(user_agent):
    if not user_agent:
        return False
    agents = ['W3C_Validator',
              'baiduspider',
              'bingbot',
              'embedly',
              'facebookexternalhit',
              'linkedinbot',
              'outbrain',
              'pinterest',
              'quora link preview',
              'rogerbot',
              'showyoubot',
              'slackbot',
              'twitterbot',
              'vkShare',
              'APIs-Google',
              'Mediapartners-Google',
              'Googlebot-Image',
              'Googlebot',
              'Googlebot-News']
    for agent in agents:
        if agent in user_agent:
            return True
    return False


def is_prerender(user_agent):
    if not user_agent:
        return False
    agents = ['prerender']
    for agent in agents:
        if agent in user_agent:
            return True
    return False


def is_bot_log(user_agent):
    if is_bot(user_agent):
        return 1
    if is_prerender(user_agent):
        return 2
    return 0


def get_ssr(path):
    origin_url = 'https://www.vibbidi.net/{0}'.format(encode_uri_component(path))
    render_server = 'https://service.prerender.cloud'
    render_url = '{0}/{1}'.format(render_server, origin_url)
    resp = request(method='GET', url=render_url, headers={
        'X-Prerender-Token': ssr_token
    })
    print('render_url: {0}'.format(render_url))
    return resp


def cache_existed(obj_type, uuid):
    if obj_type == 'single':
        return os.path.isfile(os.path.join(cache_html_path, 'singles', 'single_{0}.html'.format(uuid)))
    if obj_type == 'artist':
        return os.path.isfile(os.path.join(cache_html_path, 'artists', 'artist_{0}.html'.format(uuid)))
    if obj_type == 'album':
        return os.path.isfile(os.path.join(cache_html_path, 'albums', 'album_{0}.html'.format(uuid)))
    if obj_type == 'playlist':
        return os.path.isfile(os.path.join(cache_html_path, 'playlists', 'playlist_{0}.html'.format(uuid)))
    if obj_type == 'user':
        return os.path.isfile(os.path.join(cache_html_path, 'users', 'user_{0}.html'.format(uuid)))
    return False


def cache_from_directory(obj_type, uuid):
    if not cache_existed(obj_type, uuid):
        return None
    if obj_type == 'single':
        return send_from_directory(os.path.join(cache_html_path, 'singles'), 'single_{0}.html'.format(uuid))
    if obj_type == 'artist':
        return send_from_directory(os.path.join(cache_html_path, 'artists'), 'artist_{0}.html'.format(uuid))
    if obj_type == 'album':
        return send_from_directory(os.path.join(cache_html_path, 'albums'), 'album_{0}.html'.format(uuid))
    if obj_type == 'playlist':
        return send_from_directory(os.path.join(cache_html_path, 'playlists'), 'playlist_{0}.html'.format(uuid))
    if obj_type == 'user':
        return send_from_directory(os.path.join(cache_html_path, 'users'), 'user_{0}.html'.format(uuid))
    return None
