import random
import string
from datetime import datetime

ALPHA_NUMERIC = string.digits + string.ascii_letters


def generate_random_string(length):
    random.seed(datetime.utcnow())
    return ''.join(random.choices(ALPHA_NUMERIC, k=length))
