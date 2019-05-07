from datetime import datetime, timezone

from dateutil.relativedelta import relativedelta


def unix_time_millis(dt):
    """
    :type dt: datetime
    :rtype: int
    """
    if not dt.tzinfo:
        dt = dt.replace(tzinfo=timezone.utc)

    return int(dt.timestamp() * 1000)


def utc_from_millis(millis):
    """
    :type millis: float
    :rtype: datetime
    """
    return datetime.fromtimestamp(millis / 1000).replace(tzinfo=timezone.utc)


def lastmod_str(dt=None):
    """
    :type dt: datetime or None
    :rtype: str
    """
    if dt:
        return dt.strftime('%Y-%m-%dT%H:%M:%S') + '+00:00'

    last_mod = datetime.utcnow() + relativedelta(minutes=-14)
    return last_mod.strftime('%Y-%m-%dT%H') + ':00:00+00:00'
