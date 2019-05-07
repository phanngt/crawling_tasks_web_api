import random
from datetime import datetime


def get_random_valid_item_from_list(items):
    random.seed(datetime.utcnow())
    if not items:
        return None

    items = [item for item in items if item is not None]
    if not items:
        return None

    return items[random.randrange(len(items))]
