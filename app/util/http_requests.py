import json
import traceback
import urllib.request as urllib_request


def load_json(url):
    detail = None
    try:
        with urllib_request.urlopen(url) as response:
            if response.getcode() == 200:
                return json.loads(response.read().decode()), None
            detail = 'HTTP request failed: GET {}; Response status code = {}'.format(url, response.getcode())
            return None, detail
    except Exception as ex:
        detail = 'Runtime error: {}'.format(ex)
        print(detail)
        traceback.print_exc()
        return None, detail
    finally:
        if detail:
            print(detail)


def load_binary(url):
    detail = None
    try:
        with urllib_request.urlopen(url) as response:
            if response.getcode() == 200:
                return response.read(), None
            detail = 'HTTP request failed: GET {}; Response status code = {}'.format(url, response.getcode())
            return None, detail
    except Exception as ex:
        detail = 'Runtime error: {}'.format(ex)
        print(detail)
        traceback.print_exc()
        return None, detail
    finally:
        if detail:
            print(detail)
