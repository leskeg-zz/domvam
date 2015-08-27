# -*- coding: utf-8 -*-
# import gevent
# from gevent import monkey
# monkey.patch_all()
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from realty.models import Advert
from .downloader import ads
from .helpers import dl_image, isNum, isStr, isFloat



KEYS = settings.KEYS
VALUES = settings.VALUES
DICT1 = settings.DICT1
DICT2 = settings.DICT2

__all__ = ["downloader", "helpers"]


all = set(KEYS)
all2 = set(VALUES)
def _prepare(obj):
    if u"Адрес" in obj.keys() and not obj[u'Адрес'].strip() == "":
        # x['address'] = x[u'Адрес']
        del obj[u'Адрес']

    # if x['address'] == "":
    #     import ipdb; ipdb.set_trace()

    
    adv = set(obj.keys())

    old_keys       = list((adv & all2))
    converted_keys = [DICT2[xi] for xi in (adv & all2)]

    nonrel_adv = obj

    for key1 in obj.keys():
        if key1 in DICT2:
            nonrel_adv[DICT2[key1]] = obj[key1]
            del nonrel_adv[key1]




    filter(lambda x: x.endswith("area"), nonrel_adv.keys())
    for i in ['total_area', 'kitchen_area', 'living_area', 'number_of_rooms', 'price']: 
        if i not in nonrel_adv:
            continue

        if isStr(nonrel_adv[i]):
            nonrel_adv[i] = nonrel_adv[i].replace(",", ".")
            # print "%s: %s" % (type(nonrel_adv[i]), nonrel_adv[i])

        if isFloat(nonrel_adv[i]) and nonrel_adv[i].count(".") > 0:
            nonrel_adv[i] = float(nonrel_adv[i])
        elif isNum(nonrel_adv[i]):
            nonrel_adv[i] = int(nonrel_adv[i])

        elif isinstance(nonrel_adv[i], int):
            pass

        else:
            print "%s:%s: %s" % (i, type(nonrel_adv[i]), nonrel_adv[i])

            print "\tNOT INT: '%s',%sINT:\t%s,\tFLOAT:\t%s\tISDIGIT:%s" % (
                nonrel_adv[i], 
                (15-len(str(nonrel_adv[i])))*" ",
                isNum(nonrel_adv[i]), 
                isFloat(nonrel_adv[i]),

                nonrel_adv[i].isdigit()
            )
        if (isinstance(nonrel_adv[i], float)) and nonrel_adv[i] % 1 == 0:
            nonrel_adv[i] = int(nonrel_adv[i])

    # if "number_of_rooms" in nonrel_adv.keys():
    #     if isinstance(nonrel_adv["number_of_rooms"], (str, unicode)) and nonrel_adv["number_of_rooms"].isdigit():
    #         nonrel_adv["number_of_rooms"] = int(nonrel_adv["number_of_rooms"])
    #     else:
    #         del nonrel_adv["number_of_rooms"]
            
    return nonrel_adv


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        """
        Working process divided into some separate stages
            1. Getting last date of Advert from DB. 
        """

        FULL_IMPORT = True
        DUPS_LIMIT = 10
        __count = 0
        __dups = 0
        __page_dups = 0
        control = None
        obj_buffer = []
        obj_buffer_len = 10
        obj_buffer_len = 100

        if FULL_IMPORT:
            Advert.objects.all().delete()
            Advert._get_db().mongoengine.counters.remove({})


        it = ads()
        while True:
            try:
                # it.next()
                # print control
                obj = it.send(control)
                control = None

                if obj == {}:
                    print "EMPTY"
                    continue

                if u'\u041f\u043b\u043e\u0449 \u043a\u0443\u0445\u043d\u0438' in obj.keys():
                    # print obj["url"]
                    obj['kitchen_area'] = obj[u'\u041f\u043b\u043e\u0449 \u043a\u0443\u0445\u043d\u0438']
                    del obj[u'\u041f\u043b\u043e\u0449 \u043a\u0443\u0445\u043d\u0438']

                if obj["images_len"] == 0:
                    continue

                if (not "price" in obj.keys()) or obj["price"] == "":
                    continue


                if Advert.objects(url=obj["url"]):
                # if Advert.objects(title=obj["title"], description=obj["description"]):
                    __dups += 1
                    __page_dups += 1
                    if __page_dups >= DUPS_LIMIT and not FULL_IMPORT:
                        control = "break_page_search"
                        __page_dups = 0
                else:
                    try:
                        prep_obj = _prepare(obj)
                        print obj['url']
                        






                        _ins = Advert(** prep_obj)

                        if FULL_IMPORT:
                            obj_buffer.append(_ins)
                            if len(obj_buffer) >= obj_buffer_len:
                                Advert.objects.insert(obj_buffer)
                                obj_buffer = []

                        else:
                            _ins.save(write_concern={'w':0, 'j':False, 'wtimeout':0})

                        if prep_obj['images_len'] > 0:
                            for element in prep_obj["images"]:
                                for jit in prep_obj["images"][element]:
                                    dl_image(jit)
                            # import ipdb; ipdb.set_trace()

                        
                    except UnicodeEncodeError:
                        pass
                        # import ipdb; ipdb.set_trace()

                if __count % 100 == 0:
                    print "count: %s\tdups: %s" % (__count, __dups)
                # print "count: %s\tdups: %s\t\r" % (__count, __dups),
                __count += 1
                    


            except StopIteration:
                it.close()
                break

        if len(obj_buffer) >0:
            Advert.objects.insert(obj_buffer)

        print


