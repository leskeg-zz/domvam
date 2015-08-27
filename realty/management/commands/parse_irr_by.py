# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.conf import settings
from optparse import make_option
# from polls.models import Poll

from realty.models import Region
from realty.models import Advert, AdvertImages


KEYS = settings.KEYS
VALUES = settings.VALUES
DICT1 = {}
DICT2 = {}

for i,el in enumerate(KEYS):
    try:
        DICT1[el] = VALUES[i]
    except IndexError:
        DICT1[el] = None

# key-value flip 
DICT2 = dict(zip(DICT1.values(), DICT1.keys()))

class Command(BaseCommand):
    # args = ''
    option_list = BaseCommand.option_list + (
        make_option('--download',
            action='store_true'),
        make_option('--insert',
            action='store_true'),
    )
    help = 'Parsing irr.by realty'

    @transaction.commit_manually
    def handle(self, *args, **options):
        import sys
        sys.path.append("/home/bkmz/Dev/realty_parser/src")
        from analytics import insert as insert_irr

        mongo_objects = []

        print "Start Truncating"
        # Ad.objects.all().delete()
        Advert.objects.all().delete()
        Advert._get_db().mongoengine.counters.remove({})
        print "Truncating finished"

        COUNT = 0
        for x in insert_irr():
            # print x['url']

            # try:
            #     current_region = Region.objects.filter(name=x['region']).get()
            # except Region.DoesNotExist:
            #     print "Region not found! Skip ad"
            #     import ipdb; ipdb.set_trace()
            #     continue

            # Advert(floor=2).save()
            if u"Адрес" in x.keys() and not x[u'Адрес'].strip() == "":
                # x['address'] = x[u'Адрес']
                del x[u'Адрес']

            # if x['address'] == "":
            #     import ipdb; ipdb.set_trace()

            all = set(KEYS)
            all2 = set(VALUES)
            adv = set(x.keys())

            old_keys       = list((adv & all2))
            converted_keys = [DICT2[xi] for xi in (adv & all2)]


            nonrel_adv = x

            for key1 in x.keys():
                if key1 in DICT2:
                    nonrel_adv[DICT2[key1]] = x[key1]
                    del nonrel_adv[key1]


            # nonrel_adv['region'] = int(current_region.pk)
            nonrel_adv['region'] = x['region'].strip()

            ad_nonrel_obj = Advert(**nonrel_adv)
            # ad_nonrel_obj.save()

            mongo_objects.append(ad_nonrel_obj)

            # ad_nonrel_obj.save()

            print COUNT
            COUNT += 1

            # if COUNT >= 1000:
                # break
            

            # print x['adding_date']



            # import ipdb; ipdb.set_trace()
            # break
        
        Advert.objects.insert(mongo_objects)
        transaction.commit()

