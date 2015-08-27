# -*- coding: utf-8 -*-
from django.core.urlresolvers import resolve
from django.conf import settings

from models import Region

def header(request):

    return {
        "global_regions": Region.objects.all(),
        "regions": {
            'brest': "Брест",
            'gomel': "Гомель",
            'grodno': "Гродно",
            'minsk': "Минск",
            'mogilev': "Могилев",
            'vitebsk': "Витебск",
        }
    }

def footer(request):
    return {}

def settings_groups(request):
    return {
        "realt_cat_dict": settings.REALT_CAT_DICT,
        "realt_cat_tr": settings.REALT_CAT_TR,
        
    }