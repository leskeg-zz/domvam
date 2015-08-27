# -*- coding: utf-8 -*-
import os, os.path
from hashlib import md5

from django.conf import settings
from models import Region, Advert, Advert_Users, Currency, HEATING_CHOICES, ELECTRICITY_CHOICES, SEWERAGE_CHOICES, Profile, Ticket, Myregions
from models import Currency
from datetime import datetime, timedelta
from PIL import Image, ImageFile
import PIL
import urllib2
import json
from franchising.settings import *

# from sets import Set

from itertools import islice, chain

class QuerySetChain(object):
    """
    Chains multiple subquerysets (possibly of different models) and behaves as
    one queryset.  Supports minimal methods needed for use with
    django.core.paginator.
    """

    def __init__(self, *subquerysets):
        self.querysets = subquerysets

    def count(self):
        """
        Performs a .count() for all subquerysets and returns the number of
        records as an integer.
        """
        return sum(qs.count() for qs in self.querysets)

    def _clone(self):
        "Returns a clone of this queryset chain"
        return self.__class__(*self.querysets)

    def _all(self):
        "Iterates records in all subquerysets"
        return chain(*self.querysets)

    def __getitem__(self, ndx):
        """
        Retrieves an item or slice from the chained set of results from all
        subquerysets.
        """
        if type(ndx) is slice:
            return list(islice(self._all(), ndx.start, ndx.stop, ndx.step or 1))
        else:
            return islice(self._all(), ndx, ndx+1).next()          

def translate_to_ru2(word):
    try:
        return REALT_ACTION_DICT[word]
    except:
        return word 

def is_flat_or_new(word):
    if "flat" in word or "new" in word:
        return True
    else:
        return False

def tr_cat_type2(word):
    return cat_type_dict2[word]

def tr_number_of_rooms(word):
    if int(word) > 5:
        word = 5
    return number_of_rooms_dict[str(word)]

def tr_type_of_action_window(word):
    return type_of_action_window_dict[word]

def tr_type_of_action(word):
    return type_of_action_dict[word]


def do_filtering(query_params, order):
    ads_list = Advert_Users.objects(**query_params).order_by(order)

    if 'period__contains' in query_params:
        if query_params['period__contains'] == 'day':
            query_params['action_type'] = 'daily_rent'
        else:
            query_params['action_type'] = 'rent'
        del query_params['period__contains']

    if 'exchange' in query_params:
        if query_params['exchange'] == True:
            query_params['action_type'] = 'exchange'
        else:
            query_params['action_type'] = 'sale'
        del query_params['exchange'] 
        del query_params['action_type__contains'] 

    ads_list2 = Advert.objects(**query_params).order_by(order)
    return QuerySetChain(ads_list, ads_list2)

def create_user_profile(user):
    try:
        Profile(username=user.username,email=user.email,password='').save()
    except:
        Profile(username=user.username,email='none@domvam.by',password='').save()

    this_profile = Profile.objects.get(username=user.username)
    this_profile.save()
    return this_profile

def get_my_cards(user, _to_curr='byr'):
    user_ads =  Advert_Users.objects(username=user.username)

    my_ads = []
    for ad in user_ads:
        if ad['username'] == user.username:
            ad.price = price_convert(ad.price, ad.currency, _to_curr)
            ad.currency = _to_curr
            my_ads.append(ad)

    return my_ads

def get_my_favorites(user, _to_curr='byr', order='-images_len'):
    try:
        favorites = user.favorites
    except:
        favorites = []

    query_params = {}
    query_params[ 'id__in' ] = favorites
    ads_list = Advert_Users.objects(**query_params).order_by(order)

    for ad in ads_list:
        ad.price = price_convert(ad.price, ad.currency, _to_curr)
        ad.currency = _to_curr

    ads_list2 = Advert.objects(**query_params).order_by(order)
    
    for ad in ads_list2:
        ad.price = price_convert(ad.price, ad.currency, _to_curr)
        ad.currency = _to_curr

    my_ads = list(ads_list) + list(ads_list2)

    return my_ads

def ad_is_active(ad):
    if hasattr(ad,'expiring_date') and ad.expiring_date:
        expiring_date = ad.expiring_date
    elif hasattr(ad,'adding_date') and ad.adding_date:
        expiring_date = ad.adding_date + timedelta(days=30)
    
    if  expiring_date > datetime.now():
        return True
    else:
        return True

def price_convert(value, from_, to):  
    objects = Currency.objects.all()
    _rate = {}
    for obj in objects:
        _rate[obj['charcode'].lower()] = obj
    _rate['byr'] = {'rate': 1, "scale": 1}

    return value * float(_rate[from_]['rate']/_rate[to]['rate'])
    # response = urllib2.urlopen('http://rate-exchange.appspot.com/currency?from=' + from_ + '&to=' + to)
    # data = json.load(response)
    # return value * float(data['rate'])

def handle_add_images(f,folder):
    filename = f.name
    

    md5_obj = md5()
    for chunk in f.chunks():
        md5_obj.update(chunk)

    del chunk

    filename = "%s%s" % (md5_obj.hexdigest(), os.path.splitext(filename)[-1])


    path = os.path.join(settings.MEDIA_ROOT, str(folder), filename)
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
    if f.size > 1024000:
        #Image Compression
        img = Image.open( path )
        (imgWidthNew,imgHightNew) = img.size
        newImg = Image.new(img.mode,(imgWidthNew,imgHightNew),(0,0,0,0))
        pixels = newImg.load()
        newImg.paste (img)
        os.remove(path)
        newImg.save(path, optimize=True, quality=85)


    #medium
    img = Image.open(path)
    # wpercent = (300/float(img.size[0]))
    # hsize = int((float(img.size[1])*float(wpercent)))
    # img = img.resize((300,hsize), PIL.Image.ANTIALIAS)
    img.thumbnail((800,550), Image.ANTIALIAS)
    img.save(path[:len(path)-4] + '-medium' + path[len(path)-4:])

    #thumbnail
    img = Image.open( path )
    img.thumbnail((252,173), Image.ANTIALIAS)
    img.save(path[:len(path)-4] + '-small' + path[len(path)-4:])

    path = os.path.join(settings.STATIC_URL, settings.MEDIA_URL, str(folder), filename)
    return (path)

def remove_images(f,folder):
    path = os.path.join(settings.MEDIA_ROOT, str(folder))
    if os.path.exists(path):
        filenames_original = f.encode().split(",")
        filenames = []
        for filename in filenames_original:
            filenames.append(filename)
            filenames.append(filename[:len(filename)-4] + '-medium' + filename[len(filename)-4:])
            filenames.append(filename[:len(filename)-4] + '-small' + filename[len(filename)-4:])

        savednames = os.listdir(path)
        deletenames = list(set(savednames)-set(filenames))

        for filename in deletenames:
            os.remove(os.path.join(settings.MEDIA_ROOT, str(folder), str(filename)))

        savednames_original = os.listdir(path)
        savednames = []
        for filename in savednames_original:
            if not '-small' in filename and not '-medium' in filename:
                savednames.append(filename)

        return [os.path.join(settings.STATIC_URL, settings.MEDIA_URL, str(folder))+'/{0}'.format(i) for i in savednames]
    else:
        return

def query_lte_gte(filter_obj, mystring, query_params):
    if not filter_obj.cleaned_data[ mystring + '_min' ] is None:
        query_params[ mystring + '__gte' ] = float(filter_obj.cleaned_data[ mystring + '_min' ])
    if not filter_obj.cleaned_data[ mystring + '_max' ] is None:
        query_params[ mystring + '__lte' ] = float(filter_obj.cleaned_data[ mystring + '_max' ])

def query_lte_gte_(get_params, mystring, query_params):
    try:
        query_params[ mystring + '__gte' ] = float(get_params[ mystring + '_min' ])
    except:
        pass

    try:
        query_params[ mystring + '__lte' ] = float(get_params[ mystring + '_max' ])
    except:
        pass

def query_inside(filter_obj, mystring, query_params):
    if filter_obj.cleaned_data[ mystring ] == 'yes':   
        my_arr = [value for k, value in eval(mystring.upper() + '_CHOICES') ]
        my_list = list(my_arr)
        for element in [u"нет"]:
            if element in my_list:
                my_list.remove( element )

        query_params[ mystring + '__in' ] = my_list
