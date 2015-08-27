# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.conf import settings
from optparse import make_option

from realty.models import Currency

from lxml import objectify
from lxml import etree
import xmltodict

import requests as req


class Command(BaseCommand):
    # args = ''
    option_list = BaseCommand.option_list + (
        make_option('--parse',
            action='store_true'),
    )
    help = 'Parsing Belarus NB currency rates'

    # @transaction.commit_manually
    def handle(self, *args, **options):
        URL = "http://www.nbrb.by/Services/XmlExRates.aspx"
        data = req.get(URL)
        doc = objectify.fromstring(data.text.strip(u"\xef\xbb\xbf").encode("utf-8"))
        # doc = xmltodict.parse(data.text)

        Currency.objects.all().delete()

        _first_run = False
        if Currency.objects.count() == 0:
            _first_run = True


        for i in doc.Currency:
            _out = {
                'date':     unicode(doc.attrib['Date']),
                'doc_id':   int(i.attrib["Id"]),
                'numcode':  int(i.NumCode),
                'charcode': unicode(i.CharCode),
                'name':     i.Name.text.encode("iso-8859-1"),
                'rate':     float(i.Rate), 
                'scale':    int(i.Scale)
            }
            Currency(**_out).save()


