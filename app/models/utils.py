import base64
import re
import uuid

from sqlalchemy import func
from sqlalchemy.dialects import mysql

from app import db

START_POINT_DEFAULT = 0
ITEMS_TO_GET_DEFAULT = 20

CDN_IMAGE_ENDPOINT = 'https://aimg.vibbidi-vid.com'
CDN_USER_IMAGE_ENDPOINT = 'https://uprof.vibbidi-vid.com'

MAX_QUERY_ROWS = 200

pat_http = re.compile('^https?://', re.IGNORECASE)

SORT_LATEST = 'latest'
SORT_RANDOM = 'random'


def new_uuid4():
    return uuid.uuid4().hex.upper()


def b64_safe22(s):
    return base64.b64encode(s, b'-_')[:22].decode()


def new_uuid4_b64():
    return b64_safe22(uuid.uuid4().bytes)


def image_uri(uri):
    if not uri:
        return ''

    if pat_http.match(uri):
        return uri.strip()
    else:
        return '{}/{}'.format(CDN_IMAGE_ENDPOINT, uri).strip()


def new_vibbidi_v4_id(table_name):
    id_holder = db.session.query(func.V4.nextval_ex(
        table_name)).first()
    if id_holder:
        return id_holder[0]
    return 0


def get_cdn_domain(int_id):
    cdn = {
        0: 'berserker0.vibbidi-vid.com',
        1: 'berserker1.vibbidi-vid.com',
        2: 'berserker2.vibbidi-vid.com',
        3: 'berserker3.vibbidi-vid.com',
        4: 'berserker4.vibbidi-vid.com',
        5: 'berserker5.vibbidi-vid.com',
        6: 'berserker6.vibbidi-vid.com',
        7: 'berserker7.vibbidi-vid.com',
    }
    return cdn[int_id % 8]


def escaped_pattern(s):
    return s.replace('\\', '\\\\').replace('%', '\\%')


def escaped_search_pattern(s):
    s = s.strip()

    return s.replace('\\', '\\\\').replace('%', '\\%') + ('' if len(s) < 3 else '%')


def get_next_unique_int64(seq_name):
    seq_query = db.session.query(func.nextval_ex(seq_name).label('int64_val'))
    seq_data = seq_query.first()
    return int(seq_data.int64_val)


def validate_start_point(start_point):
    """
    :type start_point: int
    :rtype: int
    """
    if start_point < 0:
        start_point = START_POINT_DEFAULT

    return start_point


def validate_items_to_get(items_to_get):
    """
    :type items_to_get: int
    :rtype: int
    """
    if items_to_get < 0 or items_to_get > MAX_QUERY_ROWS:
        items_to_get = ITEMS_TO_GET_DEFAULT

    return items_to_get


def validate_range_limit(range_limit):
    """
    :type range_limit: int or None
    :rtype: int
    """
    if range_limit is None or range_limit < 0 or range_limit > MAX_QUERY_ROWS * 10:
        range_limit = MAX_QUERY_ROWS * 10

    return range_limit


def get_compiled_raw_mysql(cmd):
    """
    :param cmd: SQLAlchemy query or statement
    :rtype: str
    """
    if hasattr(cmd, 'statement'):
        stmt = cmd.statement
    else:
        stmt = cmd

    return stmt.compile(dialect=mysql.dialect(), compile_kwargs={"literal_binds": True})
