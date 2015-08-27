# -*- coding: utf-8 -*-

from django.db import models
from django import forms

from django.forms.widgets import MultiWidget, TextInput
from django.core.validators import ValidationError
from django.forms.widgets import Select




# TODO: move to separate file for cutsom_fields
class YearField(forms.Field):
    widget = TextInput
    
    def clean(self, value):
        #First, run general validation (will catch, for example, a blank entry
        #if the field is required
        super(YearField, self).clean(value)
        
        try:
            value = int(value)
            #TODO: allow customization of these limits
            if value < 1900 or value > 2200:
                raise Exception()
            return value
        except:
            raise ValidationError('Invalid year.')

class YearField(models.IntegerField):

    "A model field for storing years, e.g. 2012"
    def formfield(self, **kwargs):
        defaults = {'form_class': YearField}
        defaults.update(kwargs)
        
        if defaults.has_key("widget"):
            del defaults['widget']

        return super(YearField, self).formfield(**defaults)