# -*- coding: utf-8 -*-
from django import template
from realty.models import Region

register = template.Library()

@register.inclusion_tag('tag_header.html', takes_context=True)
def header(context):
    out = {
        'regions': Region.objects.all(),
    }
    # import ipdb; ipdb.set_trace()

    if context.has_key('selected_region') and context['selected_region']:
        out['selected_region'] = context['selected_region']

    return out


@register.filter
def cities_iter():
    import ipdb; ipdb.set_trace()
    for x in Region.objects.all():
        yield x
