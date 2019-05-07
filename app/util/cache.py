import os
from datetime import datetime


def get_file_last_modified(file_path):
    """
    :rtype: datetime
    """
    exists = os.path.isfile(file_path)
    if not exists:
        return None
    file_stat = os.stat(file_path)
    return datetime.fromtimestamp(file_stat.st_mtime)
