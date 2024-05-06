import jdatetime
from django.forms.utils import to_current_timezone
def date2jalali(g_date):
    return jdatetime.date.fromgregorian(date=g_date) if g_date else None


def datetime2jalali(g_date):
    if g_date is None:
        return None

    g_date = to_current_timezone(g_date)
    return jdatetime.datetime.fromgregorian(datetime=g_date)