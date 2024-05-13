from django.db.models import DateTimeField, DateField
from jalali_date_new.fields import JalaliDateTimeField, JalaliDateField
from jalali_date_new.widgets import AdminJalaliDateTimeWidget, AdminJalaliDateWidget


class JalaliDateTimeModelField(DateTimeField):
    def formfield(self, **kwargs):
        return super().formfield(
            **{
                'form_class': JalaliDateTimeField,
                "widget": AdminJalaliDateTimeWidget,
                **kwargs,
            }
        )


class JalaliDateModelField(DateField):
    def formfield(self, **kwargs):
        return super().formfield(
            **{
                'form_class': JalaliDateField,
                "widget": AdminJalaliDateWidget,
                **kwargs,
            }
        )
