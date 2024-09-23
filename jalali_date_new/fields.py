# -*- coding: utf-8 -*-
from datetime import date as datetime_date, datetime as datetime_datetime
from typing import Any

from django.conf import settings
from django.forms.fields import DateField, DateTimeField
from django.utils.encoding import force_str
from jalali_date_new.utils import datetime2jalali, to_georgian
from jdatetime import GregorianToJalali, datetime as jalali_datetime

JDATETIME_FORMAT = getattr(settings, 'JDATETIME_FORMAT', '%Y-%m-%d %H:%M:%S')


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
            return datetime2jalali(value).strftime(JDATETIME_FORMAT)
        return value

    def strptime(self, value, format):
        return jalali_datetime.strptime(force_str(value), format).togregorian()

    def clean(self, value: Any) -> Any:

        # if self.required and not value:
        #     raise ValidationError('Feild is Required')

        if not value:
            return None

        val = to_georgian(value, with_tz=True)
        return val
