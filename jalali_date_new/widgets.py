from django import forms
from django.forms.utils import to_current_timezone
from jdatetime import GregorianToJalali



class AdminJalaliDateWidget(forms.DateInput):
    template_name = "jalali_date_new/widgets/jalalidate.html"

    class Media:
        js = [
            "jalali_date_new/js/jalalidatepicker.min.js",
            "jalali_date_new/js/datepicker.js"
        ]
        css = {
            'all': 
            [
                "jalali_date_new/css/jalalidatepicker.min.css"
            ]
        }


    def __init__(self, attrs=None, format=None):
        super().__init__(attrs=attrs, format=format)

    def decompress(self, value):
        if value:
            j_date_obj = GregorianToJalali(gyear=value.year, gmonth=value.month, gday=value.day)
            date_str = '%d-%.2d-%.2d' % (j_date_obj.jyear, j_date_obj.jmonth, j_date_obj.jday)

            return date_str


class AdminJalaliTimeWidget(forms.TimeInput):
    template_name = "jalali_date_new/widgets/jalalitime.html"

    class Media:
        js = [
            "jalali_date_new/js/jalalidatepicker.min.js",
            "jalali_date_new/js/datepicker.js"
        ]
        css = {
            'all': 
            [
                "jalali_date_new/css/jalalidatepicker.min.css"
            ]
        }


    def __init__(self, attrs=None, format=None):
        super().__init__(attrs=attrs, format=format)

    def decompress(self, value):
        if value:
            value = to_current_timezone(value)

            return value.strftime("%H:%M:%S")


class AdminJalaliDateTimeWidget(forms.DateTimeInput):
    template_name = "jalali_date_new/widgets/jalalidatetime.html"

    class Media:
        js = [
            "jalali_date_new/js/jalalidatepicker.min.js",
            "jalali_date_new/js/datepicker.js"
        ]
        css = {
            'all': 
            [
                "jalali_date_new/css/jalalidatepicker.min.css"
            ]
        }


    def __init__(self, attrs=None, format=None):
        super().__init__(attrs=attrs, format=format)

    def decompress(self, value):
        if value:
            value = to_current_timezone(value)
            j_date_obj = GregorianToJalali(gyear=value.year, gmonth=value.month, gday=value.day)
            date_str = '%d-%.2d-%.2d' % (j_date_obj.jyear, j_date_obj.jmonth, j_date_obj.jday)

            return date_str + ' ' + value.time().strftime("%H:%M:%S")