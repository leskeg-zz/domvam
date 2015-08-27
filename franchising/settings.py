# -*- coding: utf-8 -*-
"""
Django settings for franchising project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from mongoengine import connect as mongo_connect
mongo_connect("localhost_realty")
# mongo_connect("localhost_new_realty")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bg39+4b0%txbt%w)k_8np9y8&lm)$my7o&c&99epav(@dn=8dh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ASSETS_DEBUG = True

ALLOWED_HOSTS = ['*']
handler404 = 'app.views.custom_404'
INTERNAL_IPS = ('127.0.0.1', '192.168.1.100')

ASSETS_ROOT = os.path.join(BASE_DIR, "static")
# UGLIFYJS_EXTRA_ARGS = ("-c", "-mt", )



# Application definition

INSTALLED_APPS = (
    'mongoadmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'social.apps.django_app.me',
    'south',
    'realty',
    'django_assets',
    # 'debug_toolbar',
    # 'debug_toolbar_mongo',
    'django_extensions',
    'django.contrib.humanize',
    'django_ajax',
    'captcha',
    'mongonaut',
)

SOCIAL_AUTH_STORAGE = 'social.apps.django_app.me.models.DjangoStorage'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    # 'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar_mongo.panel.MongoDebugPanel',
  # 'debug_toolbar.panels.profiling.ProfilingDebugPanel',
)

DEBUG_TOOLBAR_MONGO_STACKTRACES = True

ROOT_URLCONF = 'franchising.urls'

WSGI_APPLICATION = 'franchising.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "realty.context_variables.header",
    "realty.context_variables.footer",
    "realty.context_variables.settings_groups",
    'django.core.context_processors.request',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.vk.VKAppOAuth2',
    'social.backends.vk.VKOAuth2',
    'mongoengine.django.auth.MongoEngineBackend',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL  = '/'
SOCIAL_AUTH_FACEBOOK_KEY = '840957269302182'
SOCIAL_AUTH_FACEBOOK_SECRET = '23f0b98100ab06e267663a2a33bf247c'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_VK_OAUTH2_KEY = '4738106'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'tSQm1eRLx1Ji5Jrnqs8d'
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']


SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',  # <--- enable this one
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)


SESSION_ENGINE = 'mongoengine.django.sessions'
SESSION_SERIALIZER = 'mongoengine.django.sessions.BSONSerializer'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Minsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'real_static', 'media')
MEDIA_URL = 'media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = BASE_DIR
# STATIC_ROOT = ''
# STATIC_URL = 'http://192.168.1.100:8082/'
STATIC_ROOT = os.path.join(BASE_DIR, 'real_static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

FIXTURE_DIRS = ( os.path.join(BASE_DIR, "franchising", "fixtures"), )

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates/"),
)


type_of_action_dict = {
    'rent': u'Сдам',
    'sale': u'Продам',
    'exchange': u'Обмен',
    'day': u'Сдам на сутки',
}


type_of_action_window_dict = {
    'rent': u'Снять',
    'sale': u'Купить',
    'exchange': u'Обмен',
    'day': u'Снять на сутки',
}

number_of_rooms_dict = {
    "1": u'однокомнатн',
    "2": u'двухкомнатн',
    "3": u'трехкомнатн',
    "4": u'четырехкомнатн',
    "5": u'многокомнатн',
}

cat_type_dict2 = {
    "flat": u'квартир',
    "new": u'Новострой',
    "room": u'комнат',
    "house": u'дом',
    "cottage": u'Коттедж',
    "dacha": u'дач',
    "half_house": u'полдома',
    "area": u'участ',
    "garage": u'гараж',
    "parking_lot": u'машиномест',
}

REALT_CAT_DICT = {
    "living": {
        "flat":     ["new", "room", "flat"],
        "house":    ["house", "cottage", "dacha", "half_house"],
        "area":     ["area", ],
        "liv_misc": ["garage", "parking_lot", "other_liv_misc"],
    },
    "commercial": {
        "building": ["building and mansion",'pavilion','angara'],
        "premise": ['office','trade','storage','food service','production','other'],
        "land":     ["land", ],
        "business": ['internet - shops','restaurants','beauty','franchise','lease business','travel agencies','other'],
    }
}

CAT_TABS_COMMERCIAL = [('building','Здания'),('premise','Помещения'),('land','Земельные участки'),('business','Готовый бизнес')]
CAT_TYPE_COMMERCIAL = {
        'building':[('building and mansion','Здания и особняки'), ('pavilion','Павилионы'), ('angara','Ангары')],
        'premise':[('office','Офисные'),('trade','Торговые'),('storage','Складские'),('food service','Общепит и сервис'),('production','Производство'),('other','Иное')],
        'land':[],
        'business':[('internet - shops','Интернет – магазины'),('restaurants','Рестораны, кафе'),('beauty','Салоны красоты'),('franchise','Франшиза'),('lease business','Арендный бизнес'),('travel agencies','Тур агентства'),('other','Иное')],
}

REALT_CAT_DICT_ORDER_LIVING = {
    "flat":     1,
    "house":    2,
    "area":     3,
    "liv_misc": 4,
}

REALT_CAT_DICT_ORDER_COMMERCIAL = {
    "building":     1,
    "premise":     2,
    "land":         3,
    "business":     4,
}

REALT_ACTION_DICT = {
    'sale rent':        u'Продажа и Аренда', 
    'rent sale':        u'Продажа и Аренда',
    'daily_rent':       u'По суткам', 
    'rent':        u'Аренда', 
    'sale':        u'Продажа', 
    'exchange':    u'Обмен',
    'building and mansion':     u'Здания и особняки',
    'pavilion':                 u'Павилионы',
    'angara':                   u'Ангары',
    'office':                   u'Офисные',
    'trade':                    u'Торговые',
    'storage':                  u'Складские',
    'food service':             u'Общепит и сервис',
    'production':               u'Производство',
    'other':                    u'Иное',
    'internet - shops':         u'Интернет – магазины',
    'restaurants':              u'Рестораны, кафе',
    'beauty':                   u'Салоны красоты',
    'franchise':                u'Франшиза',
    'lease business':           u'Арендный бизнес',
    'travel agencies':          u'Тур агентства',
    'other':                    u'Иное',
    'internet - shops':         u'Интернет – магазины',

    "living":           u"Жилое",
    "flat":             u"Квартиры",
    "new":              u"Новостройка",
    "room":             u"Комната",
    "house":            u"Дома",
    "cottage":          u"Коттедж",
    "dacha":            u"Дача",
    "half_house":       u"Полдома",
    "area":             u"Участки",
    "liv_misc":         u"Другое",
    "garage":           u"Гараж",
    "parking_lot":      u"Машинное место",
    "other_liv_misc":   u"Другое",
    "commercial":       u"Коммерческое",
    "building":         u"Здания",
    "premise":         u"Помещения",
    "shop":             u"Магазин",
    "office":           u"Офис",
    "other_com_pr":     u"Другое",
    "land":             u"Земельные участки",
    "com_misc":         u"Прочее",
    "other_com_misc":   u"Другое",
    'business':         u'Готовый бизнес',
}

REALT_CAT_TR = {
    'building and mansion':     'Здания и особняки',
    'pavilion':                 'Павилионы',
    'angara':                   'Ангары',
    'office':                   'Офисные',
    'trade':                    'Торговые',
    'storage':                  'Складские',
    'food service':             'Общепит и сервис',
    'production':               'Производство',
    'other':                    'Иное',
    'internet - shops':         'Интернет – магазины',
    'restaurants':              'Рестораны, кафе',
    'beauty':                   'Салоны красоты',
    'franchise':                'Франшиза',
    'lease business':           'Арендный бизнес',
    'travel agencies':          'Тур агентства',
    'other':                    'Иное',
    'internet - shops':         'Интернет – магазины',

    "living":           u"Жилое",
    "flat":             u"Квартира",
    "new":              u"Новостройка",
    "room":             u"Комната",
    "house":            u"Дом",
    "cottage":          u"Коттедж",
    "dacha":            u"Дача",
    "half_house":       u"Полдома",
    "area":             u"Участок",
    "liv_misc":         u"Другое",
    "garage":           u"Гараж",
    "parking_lot":      u"Машинное место",
    "other_liv_misc":   u"Другое",
    "commercial":       u"Коммерческое",
    "building":         u"Здания",
    "premise":         u"Помещения",
    "shop":             u"Магазин",
    "office":           u"Офис",
    "other_com_pr":     u"Другое",
    "land":             u"Земельные участки",
    "com_misc":         u"Прочее",
    "other_com_misc":   u"Другое",
    'business':         u'Готовый бизнес',
}

REGION_TR = {
    "Brest":        u"Брест",
    "Brestkaya":    u"Брестская область",
    "Vitebsk":      u"Витебск",
    "Vitebskaya":   u"Витебская область",
    "Gomel":        u"Гомель",
    "Gomelskaya":   u"Гомельская область",
    "Grodnenskaya": u"Гродненская область",
    "Grodno":       u"Гродно",
    "Minsk":        u"Минск",
    "Minskaya":     u"Минская область",
    "Mogilev":      u"Могилев",
    "Mogilevskaya": u"Могилевская область",
}

MY_REGIONS = [
    u"Брест",
    u"Брестская область",
    u"Витебск",
    u"Витебская область",
    u"Гомель",
    u"Гомельская область",
    u"Гродненская область",
    u"Гродно",
    u"Минск",
    u"Минская область",
    u"Могилев",
    u"Могилевская область",
]

KEYS = [
    "number_of_rooms",
    "total_area",
    "floor",
    "number_of_floors",
    "living_area",
    "kitchen_area",
    "wall_material",
    "wc",
    "balcony_deck",
    "year_built",
    "city_phone",
    "repair",
    "furniture",
    "flooring",
    "home_appliances",
    "internet",
    "terms_of_sale",
    "ownership",
    "type_of_property",
    "type_of_house",
    "lift",
    "rooms_rent",
    "chute",
    "plot_size_in_acros",
    "electricity",
    "level_numbers",
    "plumbing",
    "heating",
    "gas",
    "sewerage",
    "roof_material",
    "forest",
    "pond",
    "apointment",
    "percentage_of_readiness",
    "outbildings",
    "garage",
    "service_type",
    "property_type",
    "parking_lot",
    "light",
    "finish",
    "deadline",
    "capacity_of_people",
    "parking_places",
    "security",
    "price_per_m2",
    "prepaynment",
    "free_planning",
    "neighbors_in_the_apartment",
    "water",
    "fence",
    "bathroom",
    "agency",
    "cellar",
    "exchange",
    "double_glazed_windows",
    "loft",
    "auction",
    "column",
    "balcony_built",
    "pets",
    "kids",
    "prescribed_persons",
    "for_students",
    "rent",
]

VALUES = [
    u"Количество комнат",
    u"Общая площадь",
    u"Этаж",
    u"Этажность",
    u"Жилая площадь",
    u"Площадь кухни",
    u"Материал стен",
    u"Санузел",
    u"Балкон / лоджия",
    u"Год постройки",
    u"Городской телефон",
    u"Ремонт",
    u"Мебель",
    u"Полы",
    u"Бытовая техника",
    u"Интернет",
    u"Условия продажи",
    u"Собственность",
    u"Вид объекта",
    u"Тип дома",
    u"Лифт",
    u"Комнат сдаётся",
    u"Мусоропровод",
    u"Площадь участка в сотках",
    u"Электричество",
    u"Количество уровней",
    u"Водопровод",
    u"Отопление",
    u"Газ",
    u"Канализация",
    u"Материал крыши",
    u"Лес",
    u"Водоем",
    u"Назначение",
    u"Процент готовности",
    u"Хоз постройки",
    u"Гараж",
    u"Тип услуги",
    u"Тип недвижимости",
    u"Машиномест",
    u"Свет",
    u"Отделка",
    u"Срок сдачи",
    u"Вместимость чел(макс)",
    u"Мест для парковки",
    u"Охрана",
    u"Цена за м2",
    u"Предоплата",
    u"Свободная планировка",
    u"Соседей в квартире",
    u"Вода",
    u"Забор",
    u"Санузел",
    u"Агентство",
    u"Погреб",
    u"Обмен",
    u"Стеклопакеты",
    u"Чердак",
    u"Возможен торг",
    u"Колонка",
    u"Хоз постройки",
    u"Домашние животные",
    u"Дети",
    u"Прописано человек",
    u"Для студентов",
    u"Посуточно",

]

DICT1 = {}
DICT2 = {}

for i,el in enumerate(KEYS):
    try:
        DICT1[el] = VALUES[i]
    except IndexError:
        DICT1[el] = None

# key-value flip 
DICT2 = dict(zip(DICT1.values(), DICT1.keys()))

