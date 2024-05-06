# -*- coding: utf-8 -*-
from typing import Any
from django.forms.fields import DateField, DateTimeField
from django.utils.encoding import force_str
from datetime import date as datetime_date, datetime as datetime_datetime
from jdatetime import GregorianToJalali, JalaliToGregorian, datetime as jalali_datetime

from jalali_date_new.utils import datetime2jalali



class JalaliDateField(DateField):
    def prepare_value(self, value):
        if isinstance(value, datetime_date):
            date_obj = GregorianToJalali(gyear=value.year, gmonth=value.month, gday=value.day)
            return '%d-%.2d-%.2d' % (date_obj.jyear, date_obj.jmonth, date_obj.jday)

        return value

    def strptime(self, value, format):
        return jalali_datetime.strptime(force_str(value), format).togregorian().date()


class JalaliDateTimeField(DateTimeField):
    def prepare_value(self, value):
        if isinstance(value, datetime_datetime):
            return datetime2jalali(value).strftime('%Y-%m-%d %H:%M:%S')
        return value

    def strptime(self, value, format):
        return jalali_datetime.strptime(force_str(value), format).togregorian()
    
    def clean(self, value: Any) -> Any:
        val = DateTimeField().clean(value)
        george_date = JalaliToGregorian(val.year, val.month, val.day).getGregorianList()
        george_datetime = datetime_datetime(year=george_date[0], month=george_date[1], day=george_date[2])
        george_datetime = george_datetime.replace(hour=val.hour, minute=val.minute, second=val.second, tzinfo=val.tzinfo)
        return george_datetime