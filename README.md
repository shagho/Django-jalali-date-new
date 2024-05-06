[![PyPi Version](https://img.shields.io/pypi/v/Django-jalali-date-new.svg)](https://pypi.python.org/pypi/Django-jalali-date-new)

# Django jalali date new

It's a django package that you can use for showing jalali calendar in admin interface and views.
This is a reconstruction of [django-jalali-date](https://github.com/a-roomana/django-jalali-date).
Thanks to [JalaliDatePicker](https://github.com/majidh1/JalaliDatePicker) for it's beautifull datepicker.


## How to use this?
First add *jalali_date_new* to your django apps:
```python
INSTALLED_APPS = [
    '...',
    'jalali_date_new',
    '...',
]
```

for use in admin:
```python
#admin.py
from django.contrib import admin
from django.db import models
from jalali_date_new.fields import JalaliDateTimeField, JalaliTimeField
from jalali_date_new.widgets import AdminJalaliDateTimeWidget, AdminJalaliTimeWidget, 
									AdminJalaliDateWidget
  

  
@admin.register(...)
class AdminModel(admin.ModelAdmin):
	formfield_overrides = {
        models.DateTimeField: 
        {
            'form_class': JalaliDateTimeField,
            "widget": AdminJalaliDateTimeWidget,
        },
    }
```

you can use this for *datefield* and *timefield*:
```python
#usage for datefield
formfield_overrides = {
        models.DateField: 
        {
            'form_class': JalaliDateField,
            "widget": AdminJalaliDateWidget,
        },
    }

#usage for timefield
formfield_overrides = {
        models.TimeField: 
        {
            "widget": AdminJalaliTimeWidget,
        },
    }

```
for use in django app:
```python
#forms.py
from django import forms
from jalali_date_new.fields import JalaliDateField, JalaliDateTimeField
from jalali_date_new.widgets import AdminJalaliDateWidget, AdminJalaliDateTime,
									AdminJalaliTime

class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = ('name', 'date', 'time', 'date_time')

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        #for date
        self.fields['date'] = JalaliDateField(label=_('date'), 
            widget=AdminJalaliDateWidget)
		
		#for time
        self.fields['time'] = forms.TimeField(label=_('time'), 
            widget=AdminJalaliTime)

		#for datetime
        self.fields['date_time'] = JalaliDateTimeField(label=_('date time'), 
            widget=AdminJalaliDateTime)
```
```python
#template
<form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>

<!-- loading directly -->
<link href="{% static 'jalali_date_new/css/jalalidatepicker.min.css' %}" rel="stylesheet">
<script src="{% static 'jalali_date_new/js/jalalidatepicker.min.js' %}" 
<script>
    jalaliDatepicker.startWatch(
        {
            separatorChars:{
                date:"-"
            },
            time: true
        }
    );
</script>

<!-- OR -->
<!-- loading by form (if used AdminJalaliDateWidget) -->
{{ form.media }}
```
