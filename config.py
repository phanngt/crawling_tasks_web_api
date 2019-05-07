import os
import urllib.parse

basedir = os.path.abspath(os.path.dirname(__file__))

if os.path.exists('config.env'):
    print('Import environment from .env file')
    for line in open('config.env'):
        clean_line = line.strip()
        eq_idx = clean_line.find('=')
        if 0 < eq_idx < len(clean_line) - 1:
            os.environ[clean_line[:eq_idx]] = clean_line[eq_idx+1:].replace("\"", "")


class Config:
    APP_NAME = os.environ.get('APP_NAME') or 'Music-Crawler'

    if os.environ.get('SECRET_KEY'):
        SECRET_KEY = os.environ.get('SECRET_KEY')
    else:
        SECRET_KEY = 'SECRET_KEY_ENV_VAR_NOT_SET'
        print('SECRET KEY ENV VAR NOT SET! SHOULD NOT SEE IN PRODUCTION')

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # Admin account
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD') or 'password'
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL') or 'longpv@gmail.com'

    REDIS_URL = os.environ.get('REDISTOGO_URL') or 'http://localhost:6379'

    urllib.parse.uses_netloc.append('redis')
    url = urllib.parse.urlparse(REDIS_URL)

    RQ_DEFAULT_HOST = url.hostname
    RQ_DEFAULT_PORT = url.port
    RQ_DEFAULT_PASSWORD = url.password
    RQ_DEFAULT_DB = 0

    CACHE_REDIS_HOST = url.hostname
    CACHE_REDIS_PORT = url.port
    CACHE_DEFAULT_TIMEOUT = 2592000  # 30 days
    CACHE_KEY_PREFIX = os.environ.get('CACHE_KEY_PREFIX') or ''

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SSL_DISABLE = (os.environ.get('SSL_DISABLE') or 'True') == 'True'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        assert os.environ.get('SECRET_KEY'), 'SECRET_KEY IS NOT SET!'


config = {
    'production': ProductionConfig,
}
