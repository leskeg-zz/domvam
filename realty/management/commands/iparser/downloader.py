# -*- coding: utf-8 -*-

from helpers import dl, parse_page
import lxml.html
from urlparse import urljoin
import logging as log
import string
import datetime

# log.basicConfig(level=log.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
log.basicConfig(level=log.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

REGIONS = [
    "http://brest.irr.by/",
    "http://vitebsk.irr.by/",
    "http://gomel.irr.by/",
    "http://grodno.irr.by/",
    "http://mogilev.irr.by/",
    "http://irr.by/",
]


_irr_skip_cats = [
    u'Зарубежная недвижимость',
    u'Коммерческая недвижимость. Продажа',
    u'Коммерческая недвижимость. Аренда',
    u'Другое',
    u'Регистрация',
]

doc_str = lxml.html.document_fromstring

STORAGE = []

class AdsIterator():
    pass

def ads():

    __count = 0
    for city in REGIONS:
        doc = doc_str(dl(urljoin(city, "/realestate/"), False).text)

        for i in doc.xpath(".//div[@class='b-menuSubCat']/ul/li[@class='switchable sale_category']/a"):
            if i.text in _irr_skip_cats:
                continue
            log.info("%s -> %s" % (i.text, i.get("href")))
            # going into category
            # import ipdb; ipdb.set_trace()
            # urljoin(DOMAIN)
            _url = urljoin(urljoin(city, i.get("href")), "page_len100/page1/")
            _cat_obj = doc_str(dl(_url, False).text)

            _res = _cat_obj.xpath(".//div[@class='b-adList']/ul[@class='filter-pages']/li/a")
            if len(_res) > 0:
                _last_page = int(_res[-2].text)
            else:
                _last_page = 1
            log.debug(_last_page)

            if _last_page == 10:

                _short_search_queries = _cat_obj.cssselect("div.colMiddle div.b-popularMark div#short_items_list.hid-o ul li a")
                _short_search_queries = [x.get("href") for x in _short_search_queries]
                log.debug(_short_search_queries)
            else:
                _short_search_queries = [i.get("href")]


            for page_search in _short_search_queries:
                for page in xrange(1, _last_page+1):
                    # print page
                    url_search_page = urljoin(urljoin(city, page_search), "page_len100/page%s/" % (page))
                    _page_obj = doc_str(dl(url_search_page, False).text)

                    # continue

                    for advert in _page_obj.xpath(".//tr[@class='advertRow']/td[@class='tdTxt']/div[@class='h3']/a"):
                        _advert_url = urljoin(city, advert.get("href"))
                        _advert_res = dl(_advert_url)
                        if _advert_res == None or _advert_res.text == "":
                            continue

                        _advert_obj = doc_str(_advert_res.text)

                        #actually parsing
                        
                        # STORAGE.append(
                        #     
                        # )
                        # STORAGE[-1]['url'] = _advert_url
                        # import ipdb; ipdb.set_trace()
                        obj = parse_page(_advert_obj, _advert_url)
                        # obj['url'] = _advert_url

                        # yield parse_page(_advert_obj)
                        value = yield obj

                        if value == "break_page_search":
                            print url_search_page
                            break
                    if value == "break_page_search":
                        print url_search_page
                        break

                    

            __count += 1
            if __count >= 2:
                pass
                # break