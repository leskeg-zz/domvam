# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
import csv
from django.utils.encoding import smart_unicode
from realty.models import Advert, Currency

CITIES = [u'Минск', u'Гомель', u'Брест', u'Витебск', u'Гродно', u'Могилев']

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Advert.objects.all().delete()
        # Advert._get_db().mongoengine.counters.remove({})
        f = open('./csv_files/base_kv_utf.csv')
        r = csv.DictReader(f, delimiter=";")
        # curs = Currency.objects.all()
        # adverts = Advert.objects({})
        # return
        for row in r:
            del_keys = []
            row_obj = {}
            for key in row:
                if key != 'id' and not isinstance(key, unicode):
                    try:
                        key = key.encode('utf-8')
                    except UnicodeDecodeError:
                        continue
                    if key not in ['terms_of_sale', 'auction',
                                   'lift', 'kitchen_area',
                                   'total_area', 'living_area',
                                   'year_built', 'floor',
                                   'number_of_floors', 'price',
                                   'region', 'city', 'microregion'] \
                            and not 'image' in key and 'description' not in key:
                        row_obj[key] = unicode(row[key].decode('utf-8'))
                    elif key == 'auction':
                        if unicode(row[key].decode('utf-8')) == u'Да':
                            row_obj[key] = True
                        else:
                            row_obj[key] = False
                    elif key == 'microregion':
                        value = unicode(row[key].decode('utf-8'))
                        row_obj[key] = value
                        row_obj['region2'] = value
                    elif key =='terms_of_sale':
                        value = unicode(row[key].decode('utf-8'))
                        if u'аренда' in value:
                            row_obj['action_type'] = 'rent'
                        elif u'обмен' in value:
                            row_obj['action_type'] = 'exchange'
                        else:
                            row_obj['action_type'] = 'sale'
                    elif key == 'lift':
                        if row[key] is not None and row[key] != '':
                            row_obj[key] = True
                        else:
                            row_obj[key] = False
                    elif key in ['year_built', 'floor', 'number_of_floors']:
                        if row[key] is not None and row[key] != '':
                            try:
                                row_obj[key] = int(row[key])
                            except ValueError:
                                continue
                    elif key in ['kitchen_area', 'total_area', 'living_area', 'price']:
                        if row[key] is not None and row[key] != '':
                            try:
                                row_obj[key] = float(row[key].replace(',', '.'))
                            except ValueError:
                                continue
                    elif 'image' in key:
                        if row_obj.get('images') is None:
                            row_obj['images'] = {'medium': [], 'thumbs': [], 'original': []}
                            row_obj['images_len'] = 0
                        if isinstance(row[key], list):
                            for image in row[key]:
                                if image != '':
                                    images_arr = image.split(',')
                                    for img in images_arr:
                                        row_obj['images']['medium'].append(img)
                                        row_obj['images']['thumbs'].append(img)
                                        row_obj['images']['original'].append(img)
                                        row_obj['images_len'] += 1
                        else:
                            if row[key] != '':
                                images_arr = row[key].split(',')
                                for img in images_arr:
                                    row_obj['images']['medium'].append(img)
                                    row_obj['images']['thumbs'].append(img)
                                    row_obj['images']['original'].append(img)
                                    row_obj['images_len'] += 1
                    elif 'description' in key:
                        if row_obj.get('description') is None:
                            row_obj['description'] = ''
                        row_obj['description'] += row[key]

                    elif key in ['region', 'city']:
                        if key == 'city':
                            value = unicode(row[key].decode('utf-8'))
                            for city in CITIES:
                                if city in value:
                                    row_obj['region'] = value
                                    break
                            if row_obj.get('region') is None:
                                row_obj['region'] = unicode(row['region'].decode('utf-8')) + u' область'
                            row_obj[key] = u'г. ' + value

                        # elif key == 'house':
                        #     if row_obj.get('address') is not None:
                        #         row_obj['address'] += u' ' + unicode(row[key].decode('utf-8'))
                        #     else:
                        #         row_obj[key] = row[key]
                        # elif key == 'address':
                        #     if row_obj.get(key) is None:
                        #         row_obj[key] = unicode(row[key].decode('utf-8'))
                        #     row_obj[key] += u' ' + unicode(row['house'].decode('utf-8'))

            row_obj['currency'] = 'usd'
            row_obj['current_status'] = 'vip_normal'
            row_obj['group'] = 'living'
            row_obj['cat_tab'] = 'flat'
            row_obj['cat_type'] = 'flat'
            adv = Advert(**row_obj)
            adv.save(write_concern={'w':0, 'j':False, 'wtimeout':0})

        # a = Advert.objects(price__exists=True, images_len__gt=1,
        #                    region__icontains=u'Гомель',
        #                    action_type__contains='sale',
        #                    group='living', cat_type_in='flat')
        a = Advert.objects(price__exists=True, images_len__gt=1,
                           region__icontains=u'Гомель',
                           action_type__contains='sale',
                           group='living',
                           cat_type__in=['flat'])
        adv_im = []
        for adv in a:
            images = adv.get('images')
            if images is not None and len(images)>1:
               adv_im.append(adv)
        print a
        # Advert.objects.insert(obj_buffer)



