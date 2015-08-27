import re
from decimal import Decimal

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.formats import number_format
from django.utils.encoding import force_text

from realty.models import Currency
from franchising.settings import *

from datetime import datetime, timedelta

register = template.Library()

@register.filter
def is_flat_or_new(word):
    if "flat" in word or "new" in word:
        return True
    else:
        return False

@register.filter
def tr_cat_type2(word):
    return cat_type_dict2[word]

@register.filter
def tr_number_of_rooms(word):
    if int(word) > 5:
        word = 5
    return number_of_rooms_dict[str(word)]

@register.filter
def tr_type_of_action_window(word):
    return type_of_action_window_dict[word]

@register.filter
def tr_type_of_action(word):
    return type_of_action_dict[word]

@register.filter
def str_contains(str1,str2):
    if str2 in str1:
        return True
    else:
        return False

@register.filter
def is_positive(list_):
    if len(list_) > 0:
        return True
    else:
        return False


@register.filter
def ad_is_active(ad):
    if hasattr(ad,'expiring_date') and ad.expiring_date:
        expiring_date = ad.expiring_date
    elif hasattr(ad,'adding_date') and ad.adding_date:
        expiring_date = ad.adding_date + timedelta(days=30)
    
    if  expiring_date > datetime.now():
        return True
    else:
        return False

@register.filter
def translate_to_ru(word):
    try:
        return DICT1[word]
    except:
        return word 

@register.filter
def translate_to_ru2(word):
    try:
        return REALT_ACTION_DICT[word]
    except:
        return word 

@register.filter
@stringfilter
def lstrip(value, arg):
    return value.lstrip(arg)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

class _Converter(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(_Converter, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def __call__(self, *args, **kwargs):
        return self
    def get_currency(self):
        if "currency_dict" in self.__dict__.keys():
            return self.currency_dict

        objects = Currency.objects.all()
        out = {}
        for obj in objects:
            out[obj['charcode']] = obj


        self.currency_dict = out
        return out

    @classmethod
    @register.filter
    def converter(value, from2, to):
        if from2 == to:
            return value

        obj = _Converter()
        obj.get_currency()

        return "123123123123211231231312"


# inspared from django humanize filter intcomma
@register.filter
def intspaces(value):
    """
    Converts an integer to a string containing spaces every three digits.
    For example, 3000 becomes '3 000' and 45000 becomes '45 000'.
    """
    # try:
    #     if not isinstance(value, (float, Decimal)):
    #         value = int(value)
    # except (TypeError, ValueError):
    #     print value
    #     return intspaces(value)
    # else:
        # return number_format(value, force_grouping=True)

    orig = force_text(value)
    new = re.sub("^(-?\d+)(\d{3})", '\g<1> \g<2>', orig)
    print new
    if orig == new:
        return new
    else:
        return intspaces(new)

@register.filter
def get_range( value ):
  """
    Filter - returns a list containing range made from given value
    Usage (in template):

    <ul>{% for i in 3|get_range %}
      <li>{{ i }}. Do something</li>
    {% endfor %}</ul>

    Results with the HTML:
    <ul>
      <li>0. Do something</li>
      <li>1. Do something</li>
      <li>2. Do something</li>
    </ul>

    Instead of 3 one may use the variable set in the views
  """
  return range( value )

@register.filter
def check_img_path(path):
    if path is not None:
        if path.startswith( '/img/' ):
            return True
    return False

@register.filter
def subtract(value, arg):
    return value - arg

@register.filter
def subtract2(value, arg):
    size = len(arg)
    if size < 20:
        return value - size
    else:
        return 0

@register.filter
def isnumeric(string):
    if unicode(string).isnumeric():
        return True
    else:
        return False

@register.filter
def get_photo_name(img_path):
    return img_path.rsplit('/',1)[1]

@register.filter
def is_false(arg): 
    return arg is False

@register.filter
def is_true(arg): 
    return arg is True

@register.filter
def is_not_bool(arg):
    if arg is True or arg is False: 
        return False
    else:
        return True

@register.filter
def is_not_unicode(arg):
    return type(arg) is not unicode

@register.filter
def lookup(d, key):
    try:
        return d[key]
    except:
        return False
