import datetime

import jdatetime
from django.forms.utils import to_current_timezone
from django.utils import timezone
from jdatetime import date as jalali_date
from jdatetime import datetime as jalali_datetime


def date2jalali(g_date):
    return jdatetime.date.fromgregorian(date=g_date) if g_date else None


def datetime2jalali(g_date):
    if g_date is None:
        return None

    g_date = to_current_timezone(g_date)
    return jdatetime.datetime.fromgregorian(datetime=g_date)


def to_shamsi(value, _format=None, sep='-'):
    if not value:
        return '-'

    # If value is a string, convert it to a datetime object
    if isinstance(value, str):
        value = value.replace(sep or '/', '-')
        try:
            if value.count(':') == 2:
                value = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
            elif value.count(':') == 1:
                value = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M')
            else:
                value = datetime.datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            return '-'  # Return '-' if the string couldn't be parsed

    if isinstance(value, datetime.datetime):
        date_obj = jalali_datetime.fromgregorian(datetime=value)
        return date_obj.strftime(_format or f'%Y{sep}%m{sep}%d %H:%M')

    elif isinstance(value, datetime.date):
        date_obj = jalali_date.fromgregorian(date=value)
        return date_obj.strftime(_format or f'%Y{sep}%m{sep}%d')

    return '-'


def to_georgian(value, _format=None, with_tz=False):
    value = value.replace('/', '-')
    if not value:
        return

    if _format is None:
        # Determine the format based on the input
        if value.count(':') == 2:
            _format = '%Y-%m-%d %H:%M:%S'
        elif value.count(':') == 1:
            _format = '%Y-%m-%d %H:%M'
        else:
            _format = '%Y-%m-%d'

    # Parse the Jalali date
    if _format == '%Y-%m-%d':
        _date = jalali_datetime.strptime(value, _format).date()
    else:
        _date = jalali_datetime.strptime(value, _format)

        # Convert to Gregorian
    gregorian_date = _date.togregorian()

    if not with_tz:
        return gregorian_date

    # Convert Gregorian date to datetime object with timezone
    # Assuming the result should be in the default Django timezone
    if _format != '%Y-%m-%d':
        # Include time part in datetime
        gregorian_datetime = timezone.make_aware(
            timezone.datetime.combine(gregorian_date, _date.time()),
            timezone.get_current_timezone()
        )
    else:
        # No time part included
        gregorian_datetime = timezone.make_aware(
            timezone.datetime.combine(gregorian_date, timezone.datetime.min.time()),
            timezone.get_current_timezone()
        )

    return gregorian_datetime
