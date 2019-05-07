AVG_READING_WPM = 203.5


def text_reading_time(text):
    """
    :type text: str or None
    :rtype: float
    """
    if text:
        return len(text.split()) / AVG_READING_WPM
    return 0


def count_words(*str_array):
    """
    :rtype: int
    """
    words = 0

    for text in str_array:
        if isinstance(text, str):
            words += len(text.split())

    return words
