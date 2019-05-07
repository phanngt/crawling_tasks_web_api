import unicodedata


def deaccent(text):
    """
    :rtype: str
    """
    if isinstance(text, bytes):
        text = text.decode('utf-8')

    if not text:
        return ''

    norm = unicodedata.normalize("NFD", text)
    result = u''.join(ch for ch in norm if unicodedata.category(ch) != 'Mn')
    return unicodedata.normalize("NFC", result)
