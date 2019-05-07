from promise import Promise


def get_data_for_caching(data):
    return data.get() if isinstance(data, Promise) else data
