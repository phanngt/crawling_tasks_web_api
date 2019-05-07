import os
from datetime import datetime
import json


def log(data):
    log_file = os.environ.get('LOG_FILE')
    filename = log_file or '/var/log/V6/Application.log'
    if os.path.exists(filename):
        append_write = 'a'
    else:
        append_write = 'w'

    data['api_version'] = '6.0'
    data['createdAt'] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    log_file = open(filename, append_write)
    log_file.write(json.dumps(data))
    log_file.write('\n')
    log_file.close()
