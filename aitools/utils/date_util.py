import datetime

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y_%m_%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY_MM_DD")

    return date_text
