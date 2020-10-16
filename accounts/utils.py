from datetime import datetime


def today(date_format='%Y%m%d', string=False):
    date = datetime.today()
    if string is False:
        return date
    return date.strftime(date_format)


def datestamp(date_format='%Y%m%d'):
    return today(date_format, string=True)
