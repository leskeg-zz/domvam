import re

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

def __active(request, data_type, data_value):
    if not isinstance(request, (str, unicode)) and  data_type in request.keys() and  request[data_type] == data_value:
        return True
    return False

# used for active in GET params 
@register.simple_tag
def active(request, data_type, data_value):
    if __active(request, data_type, data_value):
        return 'active'
    return ''

@register.simple_tag
def filter_link(request, type, value, **kwargs):
    # active part 
    active_str = ""
    if __active(request, type, value):
        active_str = "active "

    css_str = ""
    if "css_class" in kwargs.keys() and not kwargs["css_class"] == "":
        css_str = " %s" % (kwargs["css_class"])



    return """class="{active_str}filter-link{css_str}" data-type="{type}" data-value="{value}" """ \
        .format(
            type=type, 
            value=value, 
            active_str=active_str,
            css_str=css_str
        )

@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()