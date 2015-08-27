# -*- coding: utf-8 -*-

import requests as req
# import requests_cache
# requests_cache.install_cache('demo_cache')

import pickle
import os
import os.path
import urlparse
import string
import datetime
from hashlib import md5

import re

from time import strptime, mktime, struct_time

import logging as log
from django.conf import settings
BASE_DIR = settings.BASE_DIR
STATIC_ROOT = settings.STATIC_ROOT

# REGIONS = [
#     "http://brest.irr.by/",
#     # "http://vitebsk.irr.by/",
#     # "http://gomel.irr.by/",
#     # "http://grodno.irr.by/",
#     # "http://mogilev.irr.by/",
#     # "http://irr.by/",
# ]

CITIES = [
    "Минск",
    "Гродно",
    "Витебск",
    "Гомель",
    "Брест",
    "Могилев",
]

# cache folder for already downloaded documents
# PATH = "/home/bkmz/Dev/realty_parser/src/cache_files/"
PATH = os.path.join(BASE_DIR, "parse_cache/")
# IMG_PATH = "/home/bkmz/Dev/realty_parser/src/images"
# IMG_PATH = "/home/bkmz/Dev/realty/static/img"
IMG_PATH = os.path.join(STATIC_ROOT, "img")
IMG_PATH = STATIC_ROOT
COUNT = 0

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36',
}

class NoneElement():
    text = ""
    def text_content(self):
        return ""    

def isStr(txt):
    if isinstance(txt, (str, unicode)):
        return True
    return False

def isFloat(txt):
    if not isStr(txt):
        return False

    try:
        float(txt)
        return True
    except ValueError:
        return False

def isNum(txt):
    if not isStr(txt):
        return False

    if txt.isdigit():
        return True
    return False


def dl_image(uri):
    pass
    dir_name = os.path.dirname(urlparse.urlsplit(uri).path)
    filename = os.path.basename(uri)
    PATH = os.path.join(IMG_PATH, dir_name.lstrip("/"))
    if not os.path.exists(PATH):
        os.makedirs(PATH)

    if os.path.exists(os.path.join(PATH, filename)):
        return        

    r = req.get("http://irr.by"+uri, stream=True, headers=headers)

    print uri + " ",

    with open(os.path.join(PATH, filename), "wb") as hl:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                print ".",
                hl.write(chunk)

    return 


def dl(uri, cache=True):
    # cache=True
    _hash = md5(uri).hexdigest()
    log.warning(uri)

    if os.path.isfile(PATH+_hash) and cache:
        res = pickle.loads(open(PATH+_hash).read())
    else:
        # return NoneElement()
        res = req.get(uri, headers=headers)
        serialized = pickle.dumps(res)
        open(PATH+_hash, "w").write(serialized)
        open(PATH+"data_log", "a+").write("%s:\t%s\n" % (_hash, uri))

    if res.status_code == 404:
        return NoneElement()
    return res

def _convert_columns(names, values):
    out = {}
    for n, v in zip(names, values):
        n = n.replace(".", "")
        out[n] = v 

    return out

def parse_page(_page_obj, _url):
    global COUNT
    COUNT += 1
    if COUNT >= 1000:
        pass
        # raise BaseException

    try:
        (adv_title,) = _page_obj.xpath(".//div[@class='wrap']/div[@class='wrapTitleLeft']/h1")
    except ValueError:
        (adv_title,) = (NoneElement(), )
        print "No Title"
        # import ipdb; ipdb.set_trace()

    _address = [unicode(x.text_content()) for x in _page_obj.xpath(".//div[@class='b-params']/table[@id='geoData']/tr/td")]
    # import ipdb; ipdb.set_trace()
    # _address = "|".join(_address)
    log.debug("|".join(_address))

    _price = _page_obj.cssselect("b#priceSelected")
    if len(_price) > 0:
        _price = _price[0].text_content()
    log.debug(_price)

    _column_names = _page_obj.xpath(".//table[@id='mainParams']/tr/th/span") # column name
    _column_names = [unicode(x.text_content()) for x in _column_names]

    _column_values = _page_obj.xpath(".//table[@id='mainParams']/tr/td/div") # res
    _column_values = [unicode(x.text_content()) for x in _column_values]

    _columns = _convert_columns(_column_names, _column_values)

    # assert len(_column_names) == len(_column_values)

    if (len(_column_names) - len(_column_values)) > 1:
        raise BaseException("No values for column names")
        import ipdb; ipdb.set_trace()


    for name, vl in zip(_column_names, _column_values):
        log.debug("%s\t%s" % (name, vl))


    _description = _page_obj.xpath(".//div[@class='b-params']/table[@id='mainParams']/tr/td/p/span")
    if len(_description) == 0:
        _description = ""
    else:
        _description = _description[0].text_content()

        log.debug(_description)


    _phones = []
    for _phone in _page_obj.cssselect("span.ico-phone"):
        _phones.append(unicode(_phone.getparent().text_content()))

    log.debug(_phones)

    _user_attrs = []
    for _att in _page_obj.cssselect("div.wrapIcons span.ico-set:not(.ico-phone)"):
        _user_attrs.append(unicode(_att.getparent().text_content()))

    log.debug("|".join(_user_attrs))
    # if len(_user_attrs) > 0:
        # import ipdb; ipdb.set_trace()

    _min_images = []
    _med_images = []
    _orig_images = []

    for _img in _page_obj.cssselect("div.wrCaruseller ul li a img"):
        _min_images.append(unicode(_img.get("src")))
        _med_images.append(unicode(_img.get("big_src")))
        _orig_images.append(unicode(_img.get("origin_src")))

    log.debug(_min_images)

    # if len(_min_images) == 0:
    #     # _page_obj.cssselect("img#advertPhotoPreview")[0].get("origin_src")
    #     # _tmp = _page_obj.cssselect("img#advertPhotoPreview")
    #     _tmp = _page_obj.cssselect("#advertPhotoPreviewCarousel > li.first.slide.act.jcarousel-item.jcarousel-item-horizontal.jcarousel-item-1.jcarousel-item-1-horizontal > a > img")
    #     if len(_tmp) > 0:
    #         _tmp = _tmp[0]
    #         _min_images.append(unicode(_tmp.get("src")))
    #         _med_images.append(unicode(_tmp.get("big_src")))
    #         _orig_images.append(unicode(_tmp.get("origin_src")))


    _youtube_video = ""
    if _page_obj.cssselect("div.b-video iframe"):
        _youtube_video = _page_obj.cssselect("div.b-video iframe")[0].get("src")


    _adding_date = _page_obj.cssselect("div.b-infAdvert div.wrap div.floatRight p:not(.gray)")
    if len(_adding_date) == 0:
        print "len - _adding_date == 0" 
        print _url
        _adding_date = 0
    else:
        _adding_date = _adding_date[0].text_content()
        _adding_date = _adding_date.split(":")[1]
        _adding_date = _adding_date.strip()
        _adding_date = _adding_date.replace(u" г.", "")

        TRANSLATE = {
            u"января":      "January",
            u"февраля":     "February",
            u"марта":       "March",
            u"апреля":      "April",
            u"мая":         "May",
            u"июня":        "June",
            u"июля":        "July",
            u"августа":     "August",
            u"сентября":    "September",
            u"октября":     "October",
            u"ноября":      "November",
            u"декабря":     "December",
        }


        
        _adding_date_ar = _adding_date.split(" ")
        _adding_date_ar[1] = TRANSLATE[_adding_date.split(" ")[1]]
        _adding_date = " ".join(_adding_date_ar)
        _adding_date = strptime(_adding_date, "%d %B %Y")
        _adding_date = mktime(_adding_date)



    out = {
        "title":            unicode(adv_title.text_content()),
        # "address":          (_address),
        "price":            unicode(_price),
        "column_names":     _column_names ,
        "column_values":    _column_values ,
        "columns":          _columns ,
        "description":      unicode(_description),
        "phones":           (_phones),
        "user_attrs":       (_user_attrs),
        "min_images":       (_min_images),
        "med_images":       (_med_images),
        "orig_images":      (_orig_images),
        "youtube_video":    unicode(_youtube_video),
        "adding_date":      int(_adding_date),
    }
    if not _address == "":
        out['address'] = _address   


    # moved from another function.
    # Need some refactoring

    i = out
    # print "|".join(i['address'])
    # import ipdb; ipdb.set_trace()
    # print i['address'][0].split(",")[0]
    # import ipdb; ipdb.set_trace()

    # if u'Вид' in i['columns'].keys():
        # print i['url']

    # import ipdb; ipdb.set_trace()

    # adr = i['address'][0]
    if len(i['address']) > 0:
        adr = i['address'][0]
    else:
        adr = ""


    adr_ar = adr.split(",")
    # print len(adr_ar)
    # continue

    # if len(adr_ar) == 1:
    if adr_ar[0].startswith(u"г."):
        adr_ar[0] = adr_ar[0][2:]
        adr_ar[0] = adr_ar[0].strip()

    # if unicode(adr_ar[0]) in CITIES:
    #     pass
    # elif unicode(adr_ar[0]) in REGIONS:
    #     pass
    # else:
    #     adr_ar[0] = "NONE"
    # if unicode(adr_ar[0]) in 

    adr_ar = map(string.strip, adr_ar)
    



    try:

        if i['columns'][u'Электричество'] == "рядом":
            pass
            # print i['url']
    except KeyError:
        pass

    try:
        if _page_obj.xpath(".//div[@class='b-params']/table[@id='geoData']/tr[1]/td/b")[0].text.lower().startswith(u'г.'):
            region2 = _page_obj.xpath(".//div[@class='b-params']/table[@id='geoData']/tr[2]/td")[0].text
        elif u'область' in _page_obj.xpath(".//div[@class='b-params']/table[@id='geoData']/tr/td/b")[0].text.lower():
            region2 = _page_obj.xpath(".//div[@class='b-params']/table[@id='geoData']/tr/td/b")[0].text.split(',')[1].replace(u' район','').replace(' р-н','')
        else:
            region2 = ''
    except:
        region2 = ''

    out = {
        "title": i['title'],
        "region": adr_ar[0],
        # "address":  ", ".join(adr_ar[1:]),
        # "price": int(i['price'].replace(u'\xa0', "").rstrip("$")),
        "description": i['description'],
        "phones": i['phones'],
        # "user_attrs": i['user_attrs'],
        # "images": {
        #     "thumbs": i['min_images'],
        #     "original": i['orig_images'],
        # },
        # "youtube": i['youtube_video'],
        # "url": i['url'],
        "url": _url,
        "adding_date": datetime.datetime.fromtimestamp(float(i['adding_date']), None)
    }

    if not region2 == '':
        out['region2'] = region2

    if i['columns']:
        out.update(i['columns'])


    try:
        out.update({
            # "price": int(i['price'].replace(u'\xa0', "").rstrip("$")),
            "price": "".join(re.findall(re.compile(r"\d+"), i["price"])),
        })
        out['currency'] = "byr"
    except ValueError:
        pass

    if (len(i['min_images']) + len(i['med_images']) + len(i['orig_images'])) > 0:
        out.update({
        "images": {
            "thumbs": i['min_images'],
            "medium": i['med_images'],
            "original": i['orig_images'],
        }})
        out.update({
            "images_len": len(i['orig_images']),
        })
    else:
        out.update({
            "images_len": 0,
        })


    if len(i['user_attrs']) > 0:
        out.update({
            "user_attrs": i['user_attrs']
        })

    if not i['youtube_video'] == "":
        out.update({
            "yotube": i['youtube_video']
        })

    if not ", ".join(adr_ar[1:]) == "":
        out['address'] = ", ".join(adr_ar[1:])

    category = _url
    category = category.split("/")
    category = category[4:-2]


    if len(category) == 2:
        if category == ['rooms', 'exchange']:
            out['cat_type']   = 'room'
            out['action_type'] = 'exchange'
        elif category == ['rooms', 'sales']:
            out['cat_type']   = 'room'
            out['action_type'] = 'sale'
        elif category == ['rooms', 'rent']:
            out['cat_type']   = 'room'
            out['action_type'] = 'rent'

        elif category == ['exchange-flats', 'others']:
            out['cat_type']   = 'flat'
            out['action_type'] = 'exchange'
        elif category == ['exchange-flats', 'incity']:
            out['cat_type']   = 'flat'
            out['action_type'] = 'exchange'

        elif category == ['garage', 'rent']:
            out['cat_type']   = 'garage'
            out['action_type'] = 'rent'
        elif category == ['garage', 'sales']:
            out['cat_type']   = 'garage'
            out['action_type'] = 'sale'

    elif len(category) == 1:
        if category == ['new']:
            out['cat_type']   = 'new'
            out['action_type'] = 'sale'
        elif category == ['demand']:
            out['cat_type']   = 'demand'
            # out['action_type'] = ''
        elif category == ['shorttime']:
            out['cat_type']   = 'flat'
            out['action_type'] = 'daily_rent'
            out['period'] = "day"
        elif category == ['longtime']:
            out['cat_type']   = 'flat'
            out['action_type'] = 'rent'
            out['period'] = "month"
        elif category == ['garage']:
            return {}
            # continue
            # out['cat_type']   = ''
            # out['action_type'] = ''
        elif category == ['exchange-houses']:
            out['cat_type']   = 'house'
            out['action_type'] = 'exchange'
        elif category == ['exchange-flats']:
            out['cat_type']   = 'flat'
            out['action_type'] = 'exchange'
        elif category == ['sale-houses']:
            out['cat_type']   = 'house'
            out['action_type'] = 'sale'
        elif category == ['sale-flats']:
            out['cat_type']   = 'flat'
            out['action_type'] = 'sale'
        elif category == ['rent-houses']:
            out['cat_type']   = 'house'
            out['action_type'] = 'rent'


    out['parsed_from'] = "irrby"
    out['group'] = "living"
    
        







        

    return out

    # coll.save(out)
    # break
    


    # if u'Количество комнат' in i['columns'].keys() and u'Комнат сдаётся' in i['columns'].keys():
    #     if not i['columns'][u'Количество комнат'] == i['columns'][u'Комнат сдаётся']:
    #         print i['url']
    #         # for k,v in i['columns'].iteritems(): 
    #             # print "%s: %s" % (k, v)

    

