from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


def get_argentina_datetime():
    current_utc_time = datetime.utcnow()

    utc_timezone = ZoneInfo('UTC')

    argentina_timezone = ZoneInfo('America/Argentina/Buenos_Aires')
    return current_utc_time.replace(tzinfo=utc_timezone).astimezone(argentina_timezone)


def get_argentina_time():
    return get_argentina_datetime().time()
