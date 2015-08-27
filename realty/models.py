# -*- coding: utf-8 -*-

import mongoengine as mongo

from django.db import models
from django.shortcuts import get_object_or_404
from .custom_fields import YearField
from datetime import datetime
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["realty.custom_fields.YearField"])

# Create your models here.

class RegionQuerySet(models.query.QuerySet):
    def dict_all(self):
        out = {}
        for x in self.all():
            out[x.pk] = x

        return out

    def get404(self):
        return get_object_or_404(self)
        

class RegionManager(models.Manager):
    def get_queryset(self):
        return RegionQuerySet(self.model, using=self._db)

    def dict_all(self):
        return self.get_queryset().dict_all()

class Region(models.Model):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    parent_region = models.ForeignKey("self", blank=True, null=True)

    # Override Manager. And QuerySet
    objects = RegionManager()

    def __unicode__(self):
        return self.name

    @classmethod
    def get_choices(cls):
        import ipdb; ipdb.set_trace()
        return ((0, 'test'),(0, 'test'),(0, 'test'),(0, 'test'),)


# class AdManager(models.Manager):
#     def get_queryset(self, *args, **kwargs):
#         # import ipdb; ipdb.set_trace()
#         queryset = super(AdManager, self).get_queryset(*args, **kwargs)

#         import ipdb; ipdb.set_trace()

#         return queryset




# class Ad(models.Model):
#     region = models.ForeignKey(Region)
#     title = models.CharField(max_length=255, null=True)

#     attrs = None

#     # objects = AdManager()


#     @property
#     def attributes(self): 
#        return Ad_attributes.objects.filter(ad_pk=self.pk).get()


#     def __unicode__(self):
#         return self.title or u"No Title"

# @receiver(post_init)
# def my_callback(sender, **kwargs):
#     print("Request finished!")

WC_TYPE = (
    (0, 'Separate'),
    (1, 'Merge'),
)

ACTION = (
    (0, 'Rent'),
    (1, 'Sale'),
)

# class Attr(models.Model):
#     object_type          = models.ForeignKey('Object_type')
#     street               = models.CharField(max_length=255)
#     house                = models.IntegerField(blank=True, null=True)
#     rooms_amount         = models.IntegerField()
#     living_space         = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True) # max resolution 1 000 000.00
#     # year_of_construction = YearField()
#     year_of_construction = models.IntegerField(blank=True, null=True) # TODO: rewrite to real worked YearField
#     floors_amount        = models.IntegerField()
#     floor                = models.IntegerField()
#     kitchen_space        = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
#     wc_type              = models.IntegerField(choices=WC_TYPE)
#     action_type          = models.IntegerField(choices=ACTION)

#     ad_obj               = models.OneToOneField(Ad, blank=True, null=True) # null and blank added for South. 

class Object_type(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

# MongoDD CHOICES

__TRUE_FALSE_CHOICES = (
    (True,  'есть'),
    (False, 'нет'),
)

__TRUE_FALSE_NEAR_CHOICES = (
    (0, "нет"),
    (1, "есть"),
    (2, "рядом"),
)

WALL_MATERIAL_CHOICES = (
    (0, u'--'),
    (1, u'белый кирпич'),
    (2, u'дерево'),
    (3, u'сруб'),
    (4, u'блочный'),
    (5, u'дерево, обложенное кирпичом'),
    (6, u'красный кирпич'),
    (7, u'керамзито-бетон'),
    (8, u'сборно-щитовой'),
    (9, u'шлакобетон'),
    (10, u'панельный'),
    (11, u'облицовочный кирпич'),
    (12, u'кирпичный'),
    (13, u'каркасный'),
    (14, u'монолитный'),
    (15, u'блок-комнаты'),
    (16, u'кирпич'),
    (17, u'силикатно-блочный'),
    (18, u'каркасно-блочный'),
    (19, u'панель'),
    (20, u'м.кр.'),
    (21, u'кр.б.'),
    (22, u'деревянный'),
    (23, u'дерево+кирпич'),
    (24, u'бл-к'),
    (25, u'монолит'),
    (26, u'ж/б каркас+блоки'),
    (27, u'ж/б каркас/блоки'),
    (28, u'каркас'),
)

WC_CHOICES = (
    (0, u'нет'),
    (1, u'раздельный'),
    (2, u'совмещенный'),
    (3, u'2 санузла'),
    (4, u'3 санузла'),
    (5, u'панельный'),
    (6, u'кирпичный'),
)

BALCONY_DECK_CHOICES = (
    (0, u'нет'),
    (1, u'балкон незастекленный'),
    (2, u'лоджия незастекленная'),
    (3, u'балкон застекленный'),
    (4, u'лоджия застекленная'),
    (5, u'терраса'),
)

CITY_PHONE_CHOICES = __TRUE_FALSE_CHOICES

REPAIR_CHOICES = (
    (0, u'--'),
    (1, u'евроремонт'),
    (2, u'отличный ремонт'),
    (3, u'хороший ремонт'),
    (4, u'нормальный ремонт'),
    (5, u'удовлетворительный ремонт'),
    (6, u'плохое состояние'),
    (7, u'строительная отделка'),
    (8, u'без отделки'),
    (9, u'аварийное состояние'),
)

FURNITURE_CHOICES = __TRUE_FALSE_CHOICES

FLOORING_CHOICES = (
    (0, u'деревянные'),
    (1, u'ламинирование'),
    (2, u'паркет'),
    (3, u'линолеум'),
    (4, u'ковровое покрытие'),
    (5, u'ДСП'),
)

HOME_APPLIANCES_CHOICES = __TRUE_FALSE_CHOICES

INTERNET_CHOICES = __TRUE_FALSE_CHOICES

TERMS_OF_SALE_CHOICES = (
    (0, 'свободная квартира'),
    (1, 'обмен'),
    (2, 'чистая продажа'),
    (3, 'обмен-съезд'),
    (4, 'обмен-разъезд'),
    (5, 'подбираются варианты'),
)

OWNERSHIP_CHOICES = (
    (0, 'частная'),
    (1, 'гос.-приватизированная'),
    (2, 'ЖСК'),
    (3, 'долевое строительство'),
    (4, 'государственная'),
    (5, 'ведомственная'),
)

TYPE_OF_PROPERTY_CHOICES = (
    (0, 'гараж'),
    (1, 'дом'),
    (2, 'дача'),
    (3, 'коттедж'),
    (4, 'участок'),
    (5, 'полдома'),
    (6, 'Дача'),
    (7, 'Коттедж'),
    (8, 'Дом'),
    (9, 'Дача-коттедж'),
    (10, 'Участок'),
    (11, 'стоянка'),
    (12, 'бокс'),
    (13, 'Часть дома'),
    (14, 'часть дома'),
    (15, 'Коробка дома'),
    (16, '1/2 дома'),
    (17, 'Дом-дача'),
    (18, 'блок'),
    (19, '1/4 дома'),
    (20, 'Жилой дом'),
    (21, '1/2 доля дома'),
    (22, 'Коробка коттеджа'),
    (23, 'Нулевой цикл'),
)

TYPE_OF_HOUSE_CHOICES = (
    (0, u'хрущевка'),
    (1, u'чешский проект'),
    (2, u'улучшенный проект'),
    (3, u'стандартный проект'),
    (4, u'сталинка'),
    (5, u'брежневка'),
    (6, u'малосемейка'),
)

LIFT_CHOICES = __TRUE_FALSE_CHOICES

CHUTE_CHOICES = __TRUE_FALSE_CHOICES

ELECTRICITY_CHOICES = __TRUE_FALSE_NEAR_CHOICES

PLUMBING_CHOICES = (
    (0, 'да'),
    (1, 'нет'),
    (2, 'холодная'),
    (3, 'рядом'),
    (4, 'рядом колодец'),
    (5, 'горячая'),
)

HEATING_CHOICES = (
    (0, u'да'),
    (1, u'печное'),
    (2, u'нет'),
    (3, u'паровое на твердом топливе'),
    (4, u'электрическое'),
    (5, u'паровое на газу'),
    (6, u'центральное'),
    (7, u'паровое'),
    (8, u'паровое на жидком топливе'),
)

GAS_SHOICES = __TRUE_FALSE_NEAR_CHOICES

SEWERAGE_CHOICES = (
    (0, 'нет'),
    (1, 'да'),
    (2, 'с/у на улице'),
    (3, 'местная'),
    (4, 'центральная'),
    (5, 'центральая'),
)

ROOF_MATERIAL_CHOICES = (
    (0, 'шифер'),
    (1, 'ондулин'),
    (2, 'металло-черепица'),
    (3, 'черепица'),
    (4, 'жесть'),
    (5, 'рубероид'),
    (6, 'доски'),
)

FOREST_CHOICES = __TRUE_FALSE_CHOICES

POND_CHOICES = __TRUE_FALSE_CHOICES

APOINTMENT_CHOICES = (
    (0, 'дача'),
    (1, 'ИЖС'),
    (2, 'коммерческое'),
)

OUTBILDINGS_CHOICES = __TRUE_FALSE_CHOICES

GARAGE_CHOICES = __TRUE_FALSE_CHOICES

SERVICE_TYPE_CHOICES = (
    (0, "куплю"),
    (1, "сниму"),
)

PROPERTY_TYPE_CHOICES = (
    (0, 'коммерческая недвижимость'),
    (1, 'квартира'),
    (2, 'дом, дача, коттедж'),
    (3, 'гараж, машиноместо'),
    (4, 'комната'),
    (5, 'участок'),
)

PARKING_LOT_CHOICES = (
    (0, '1'),
    (1, '2'),
    (2, '3'),
    (3, '&gt;3'),
)

LIGHT_CHOICES = __TRUE_FALSE_CHOICES

FINISH_CHOICES = (
    (0, 'без отделки'),
    (1, 'с отделкой'),
    (2, 'cтроительная отделка'),
    (3, 'отличный ремонт'),
    (4, 'евроремонт'),
    (5, 'удовлетворительный ремонт'),
    (6, 'хороший ремонт'),
)

DEADLINE_CHOICES = (
    (0, 'длительный'),
    (1, 'сутки/часы'),
)

SECURITY_CHOICES = __TRUE_FALSE_CHOICES

PREPAYNMENT_CHOICES = (
    (0, 'не нужна'),
    (1, '1 месяц'),
    (2, '2 месяца'),
    (3, '3 месяца'),
)

FREE_PLANNING_CHOICES = __TRUE_FALSE_CHOICES

NEIGHBORS_IN_THE_APARTMENT_CHOICES = (
    (0, '1'),
    (1, '3'),
    (2, 'нет'),
    (3, '2'),
    (4, '1 девушка'),
)

WATER_CHOICES = __TRUE_FALSE_CHOICES


# Misc models options


# @TODO fields:
# ACRES Field
# RANGE Field
# TRUE\FALSE Field

# MongoDB Collections
class Ticket(mongo.DynamicDocument):
    name = mongo.fields.StringField(required=False)
    email = mongo.fields.EmailField(required=False)
    phone = mongo.fields.StringField(required=False)
    text = mongo.fields.StringField(required=False)

class Profile(mongo.DynamicDocument):
    username = mongo.fields.StringField(unique=True, required=True)
    email = mongo.fields.EmailField(unique=True, required=True)
    password = mongo.fields.StringField(required=True)

class User(mongo.DynamicDocument):
    username = mongo.fields.StringField(unique=True, required=True)
    email = mongo.fields.EmailField(unique=True, required=True)
    # password = mongo.fields.StringField(required=True)
    is_active = mongo.fields.BooleanField(required=False)
    is_staff = mongo.fields.BooleanField(required=False)
    is_superuser = mongo.fields.BooleanField(required=False)
    date_joined = mongo.fields.DateTimeField(required=False)
    last_login = mongo.fields.DateTimeField(required=False)

class ProfileAgency(mongo.DynamicDocument):
    username = mongo.fields.StringField(unique=True, required=True)
    email = mongo.fields.EmailField(unique=True, required=True)
    password = mongo.fields.StringField(required=True)
    name_of_entity = mongo.fields.StringField(unique=False, required=True)
    head_name = mongo.fields.StringField(unique=False, required=True)
    head_position = mongo.fields.StringField(unique=False, required=True)
    country = mongo.fields.StringField(unique=False, required=True)
    locality = mongo.fields.StringField(unique=False, required=True)
    region = mongo.fields.StringField(unique=False, required=True)
    post_code = mongo.fields.StringField(unique=False, required=True)
    street = mongo.fields.StringField(unique=False, required=True)
    house_number_body = mongo.fields.StringField(unique=False, required=True)
    office_number_room_apartment = mongo.fields.StringField(unique=False, required=True)
    mail_adress = mongo.fields.StringField(unique=False, required=True)
    contact_phone = mongo.fields.StringField(unique=False, required=True)
    mobile_phone = mongo.fields.StringField(unique=False, required=False)
    fax = mongo.fields.StringField(unique=False, required=False)
    extra_email = mongo.fields.StringField(unique=False, required=False)
    UNP_organization = mongo.fields.StringField(unique=False, required=True)
    registering_autority = mongo.fields.StringField(unique=False, required=True)
    number_state_registration = mongo.fields.StringField(unique=False, required=False)
    date_state_registration = mongo.fields.StringField(unique=False, required=True)

class AdvertImages(mongo.EmbeddedDocument):
    thumbs = mongo.fields.ListField(mongo.fields.URLField())
    original = mongo.fields.ListField(mongo.fields.URLField())

class Myregions(mongo.DynamicDocument):
    NAME = mongo.fields.StringField(required=False)
    OBL = mongo.fields.StringField(required=False)
    RAION = mongo.fields.StringField(required=False)

class Cities(mongo.DynamicDocument):
    SOATO = mongo.fields.IntField(required=False)
    PREF = mongo.fields.StringField(required=False)
    NAME = mongo.fields.StringField(required=False)
    OBL = mongo.fields.StringField(required=False)
    RAION = mongo.fields.StringField(required=False)
    SOVET = mongo.fields.StringField(required=False)

class Streets(mongo.DynamicDocument):
    SOATO = mongo.fields.IntField(required=False)
    KUL = mongo.fields.IntField(required=False)
    UDS_105 = mongo.fields.IntField(required=False)
    NTU = mongo.fields.StringField(required=False)
    ULICA = mongo.fields.StringField(required=False)

class Advert_Users(mongo.DynamicDocument):
    action_type = mongo.fields.StringField(required=False)

    cat_tab = mongo.fields.StringField(required=False)
    cat_type = mongo.fields.StringField(required=False)
    price = mongo.fields.IntField(required=False)
    currency = mongo.fields.StringField(choices=(('usd','usd'),('eur','eur'),('byr','byr')),required=False)
    doc_id = mongo.fields.SequenceField(unique=True, required=True)
    adding_date = mongo.fields.DateTimeField(default= lambda: datetime.now())
    expiring_date = mongo.fields.DateTimeField(required=False)
    prepayment = mongo.fields.IntField(required=False)
    double_glazed_windows = mongo.fields.BooleanField(required=False)
    neighbors_in_the_apartment = mongo.fields.IntField(required=False)
    area = mongo.fields.IntField(required=False)
    plot_size_in_acros = mongo.fields.FloatField(required=False)
    households_built = mongo.fields.IntField(required=False)
    heating = mongo.fields.StringField(required=False)
    parking_places = mongo.fields.StringField(required=False)
    km_from_city = mongo.fields.IntField(required=False)
    electricity = mongo.fields.BooleanField(required=False)
    balcony_built = mongo.fields.BooleanField(required=False)
    # exchange_description = mongo.fields.StringField(required=False)
    group = mongo.fields.StringField(required=False)
    description = mongo.fields.StringField(required=False)
    region = mongo.fields.StringField(required=False)
    microregion = mongo.fields.StringField(required=False)
    city = mongo.fields.StringField(required=False)
    address = mongo.fields.StringField(required=False)
    house = mongo.fields.StringField(required=False)
    year_built = mongo.fields.IntField(required=False)
    floor = mongo.fields.IntField(required=False)
    number_of_rooms = mongo.fields.IntField(required=False)
    number_of_floors = mongo.fields.IntField(required=False)
    kitchen_area = mongo.fields.FloatField(required=False)
    total_area = mongo.fields.FloatField(required=False)
    living_area = mongo.fields.FloatField(required=False)
    balcony_deck = mongo.fields.StringField(required=False)
    wall_material = mongo.fields.StringField(required=False)
    wc = mongo.fields.StringField(required=False)
    flooring = mongo.fields.StringField(required=False)
    repair = mongo.fields.StringField(required=False)
    home_appliances = mongo.fields.BooleanField(required=False)
    period = mongo.fields.StringField(required=False)
    # images = mongo.fields.StringField(required=False)
    # agreement = mongo.fields.BooleanField(required=False)
    exchange = mongo.fields.BooleanField(required=False)
    security = mongo.fields.BooleanField(required=False)
    for_students = mongo.fields.BooleanField(required=False)
    rent = mongo.fields.BooleanField(required=False)
    finish = mongo.fields.BooleanField(required=False)
    city_phone = mongo.fields.BooleanField(required=False)
    lift = mongo.fields.BooleanField(required=False)
    kids = mongo.fields.BooleanField(required=False)
    pets = mongo.fields.BooleanField(required=False)
    title = mongo.fields.StringField(required=False)
    fence = mongo.fields.BooleanField(required=False)
    column = mongo.fields.BooleanField(required=False)
    cellar = mongo.fields.BooleanField(required=False)
    garage = mongo.fields.BooleanField(required=False)
    loft = mongo.fields.BooleanField(required=False)
    bathroom = mongo.fields.BooleanField(required=False)
    sewerage = mongo.fields.BooleanField(required=False)
    light = mongo.fields.BooleanField(required=False)
    gas = mongo.fields.BooleanField(required=False)
    internet = mongo.fields.BooleanField(required=False)
    furniture = mongo.fields.BooleanField(required=False)
    auction = mongo.fields.BooleanField(required=False)
    contact_name = mongo.fields.StringField(required=False)
    # phones = mongo.fields.StringField(required=False)
    phones2 = mongo.fields.StringField(required=False)
    phones3 = mongo.fields.StringField(required=False)
    status = mongo.fields.BooleanField(required=False)
    owner = mongo.fields.StringField(required=False)
    url = mongo.fields.URLField(required=False)

    @classmethod
    def get_cat_tab_choices(self, group):
        from django.conf import settings
        cat_dict = settings.REALT_CAT_DICT
        cat_tr = settings.REALT_CAT_TR

        if group=="living":
            cat_dict_order = settings.REALT_CAT_DICT_ORDER_LIVING
        elif group=="commercial":
            cat_dict_order = settings.REALT_CAT_DICT_ORDER_COMMERCIAL

        out = []
        ordered_keys = sorted(cat_dict[group].keys(), key=lambda x: cat_dict_order[x])
        for k in ordered_keys:
            out.append((k, cat_tr[k]))
        out = tuple(out)
        return out

    @classmethod
    def get_cat_type_choices(self, group=None, tab=None):
        from django.conf import settings
        cat_dict = settings.REALT_CAT_DICT
        cat_tr = settings.REALT_CAT_TR

        if not group in cat_dict.keys() or not tab in cat_dict[group].keys():
            return ()

        out = []
        for k in cat_dict[group][tab]:
            out.append((k, cat_tr[k]))

        out = tuple(out)
        return out
        
        # return (('house', u"Дом"), ('room', u"Комната"), ('flat', u"Хата"))

    @classmethod
    def get_action_choices(self):
        from django.conf import settings
        act_dict = settings.REALT_ACTION_DICT

        out = []
        for k in act_dict:
            out.append((k, act_dict[k]))

        out = tuple(out)
        return out


    @classmethod
    def get_region_choices(cls):
        return ((x, x) for x in cls.objects.distinct('region'))    

    # using for tempalte rendering
    def get(self, key):
        return self[key]


    def clean111 (self):
        if not self.percentage_of_readiness ==None:
            msg_per_read = "percentage_of_readiness might be only int or long(> 6 chars) string"
            try:
                if not isinstance(int(self.percentage_of_readiness), int):
                    raise ValidationError(msg_per_read)
            except ValueError:
                raise ValidationError(msg_per_read)



class Advert(mongo.DynamicDocument):
    action_type = mongo.fields.StringField(required=False)

    cat_tab = mongo.fields.StringField(required=False)
    cat_type = mongo.fields.StringField(required=False)
    price = mongo.fields.IntField(required=False)
    currency = mongo.fields.StringField(choices=(('usd','usd'),('eur','eur'),('byr','byr')),required=False)
    doc_id = mongo.fields.SequenceField(unique=True, required=True)
    adding_date = mongo.fields.DateTimeField(default= lambda: datetime.now())
    expiring_date = mongo.fields.DateTimeField(required=False)
    prepayment = mongo.fields.IntField(required=False)
    double_glazed_windows = mongo.fields.BooleanField(required=False)
    neighbors_in_the_apartment = mongo.fields.IntField(required=False)
    area = mongo.fields.IntField(required=False)
    plot_size_in_acros = mongo.fields.FloatField(required=False)
    households_built = mongo.fields.IntField(required=False)
    heating = mongo.fields.StringField(required=False)
    parking_places = mongo.fields.StringField(required=False)
    km_from_city = mongo.fields.IntField(required=False)
    electricity = mongo.fields.BooleanField(required=False)
    balcony_built = mongo.fields.BooleanField(required=False)
    # exchange_description = mongo.fields.StringField(required=False)
    group = mongo.fields.StringField(required=False)
    description = mongo.fields.StringField(required=False)
    region = mongo.fields.StringField(required=False)
    microregion = mongo.fields.StringField(required=False)
    city = mongo.fields.StringField(required=False)
    address = mongo.fields.StringField(required=False)
    house = mongo.fields.StringField(required=False)
    year_built = mongo.fields.IntField(required=False)
    floor = mongo.fields.IntField(required=False)
    number_of_rooms = mongo.fields.IntField(required=False)
    number_of_floors = mongo.fields.IntField(required=False)
    kitchen_area = mongo.fields.FloatField(required=False)
    total_area = mongo.fields.FloatField(required=False)
    living_area = mongo.fields.FloatField(required=False)
    balcony_deck = mongo.fields.StringField(required=False)
    wall_material = mongo.fields.StringField(required=False)
    wc = mongo.fields.StringField(required=False)
    flooring = mongo.fields.StringField(required=False)
    repair = mongo.fields.StringField(required=False)
    home_appliances = mongo.fields.BooleanField(required=False)
    period = mongo.fields.StringField(required=False)
    # images = mongo.fields.StringField(required=False)
    # agreement = mongo.fields.BooleanField(required=False)
    exchange = mongo.fields.BooleanField(required=False)
    security = mongo.fields.BooleanField(required=False)
    for_students = mongo.fields.BooleanField(required=False)
    rent = mongo.fields.BooleanField(required=False)
    finish = mongo.fields.BooleanField(required=False)
    city_phone = mongo.fields.BooleanField(required=False)
    lift = mongo.fields.BooleanField(required=False)
    kids = mongo.fields.BooleanField(required=False)
    pets = mongo.fields.BooleanField(required=False)
    title = mongo.fields.StringField(required=False)
    fence = mongo.fields.BooleanField(required=False)
    column = mongo.fields.BooleanField(required=False)
    cellar = mongo.fields.BooleanField(required=False)
    garage = mongo.fields.BooleanField(required=False)
    loft = mongo.fields.BooleanField(required=False)
    bathroom = mongo.fields.BooleanField(required=False)
    sewerage = mongo.fields.BooleanField(required=False)
    light = mongo.fields.BooleanField(required=False)
    gas = mongo.fields.BooleanField(required=False)
    internet = mongo.fields.BooleanField(required=False)
    furniture = mongo.fields.BooleanField(required=False)
    auction = mongo.fields.BooleanField(required=False)
    contact_name = mongo.fields.StringField(required=False)
    # phones = mongo.fields.StringField(required=False)
    phones2 = mongo.fields.StringField(required=False)
    phones3 = mongo.fields.StringField(required=False)
    status = mongo.fields.BooleanField(required=False)
    owner = mongo.fields.StringField(required=False)
    url = mongo.fields.URLField(required=False) 

    # captcha = CaptchaField(widget=StyleCaptchaTextInput(), required=True)
    # captcha = CaptchaField()

    # # name = mongo.fields.StringField(widget=mongo.fields.TextInput(attrs={"placeholder": "Ваше имя"}))
    # # email = mongo.fields.StringField(widget=mongo.fields.EmailInput(attrs={"placeholder": "E-mail"}))
    # month = mongo.fields.BooleanField(widget=StyleCheckbox(label = u"Длительная"), required=False)
    # day = mongo.fields.BooleanField(widget=StyleCheckbox(label = u"По суткам"), required=False)
    # exchange = mongo.fields.BooleanField(widget=StyleCheckbox(label = u"Обмен"), required=False)
    # ad_pk                           = mongo.fields.LongField()
    # number_of_rooms                 = mongo.fields.IntField(min_value=-1, max_value=10) # Количество комнат
    # total_area                      = mongo.fields.DecimalField(min_value=0, precision=2) # Общая площадь
    # floor                           = mongo.fields.IntField(min_value=-1, max_value=64) # Этаж
    # number_or_floors                = mongo.fields.IntField(min_value=1,  max_value=64) # Этажность
    # living_area                     = mongo.fields.DecimalField(min_value=0, precision=2) # Жилая площадь
    # kitchen_area                    = mongo.fields.DecimalField(min_value=0, precision=2) # Площадь кухни
    # wall_material                   = mongo.fields.StringField(choices=WALL_MATERIAL_CHOICES) # Материал стен
    # wc                              = mongo.fields.StringField(choices=WC_CHOICES) # Санузел
    # images                          = mongo.EmbeddedDocumentField("AdvertImages") # 
    # balcony_deck                    = mongo.fields.StringField(choices=BALCONY_DECK_CHOICES) # Балкон / лоджия
    # year_built                      = mongo.fields.IntField(min_value=1, max_value=lambda: datetime.datetime.now().year) # Год постройки
    # city_phone                      = mongo.fields.BooleanField(choices=CITY_PHONE_CHOICES) # Городской телефон
    # repair                          = mongo.fields.StringField(choices=REPAIR_CHOICES) # Ремонт
    # furniture                       = mongo.fields.BooleanField(choices=FURNITURE_CHOICES) # Мебель
    # flooring                        = mongo.fields.StringField(choices=FLOORING_CHOICES) # Полы
    # home_appliances                 = mongo.fields.BooleanField(choices=HOME_APPLIANCES_CHOICES) # Бытовая техника
    # internet                        = mongo.fields.BooleanField(choices=INTERNET_CHOICES) # Интернет
    # terms_of_sale                   = mongo.fields.StringField(choices=TERMS_OF_SALE_CHOICES) # Условия продажи
    # ownership                       = mongo.fields.StringField(choices=OWNERSHIP_CHOICES) # Собственность
    # type_of_property                = mongo.fields.StringField(choices=TYPE_OF_PROPERTY_CHOICES) # Вид объекта
    # type_of_house                   = mongo.fields.StringField(choices=TYPE_OF_HOUSE_CHOICES) # Тип дома
    # lift                            = mongo.fields.BooleanField(choices=LIFT_CHOICES) # Есть ли лифт
    # rooms_rent                      = mongo.fields.IntField(min_value=1, max_value=10) # Комнат сдаётся
    # chute                           = mongo.fields.BooleanField(choices=CHUTE_CHOICES) # Мусоропровод
    # # address_2                     = mongo.fields. # Адрес
    # plot_size_in_acros              = mongo.fields.DecimalField(min_value=0, precision=2) # Площадь участка в сотках
    # electricity                     = mongo.fields.StringField(choices=ELECTRICITY_CHOICES) # Электричество
    # level_numbers                   = mongo.fields.IntField(min_value=1, max_value=10) # Количество уровней
    # plumbing                        = mongo.fields.StringField(choices=PLUMBING_CHOICES) # Водопровод
    # heating                         = mongo.fields.StringField(choices=HEATING_CHOICES) # Отопление
    # gas                             = mongo.fields.StringField(choices=GAS_SHOICES) # Газ
    # sewerage                        = mongo.fields.StringField(choices=SEWERAGE_CHOICES) # Канализация
    # roof_material                   = mongo.fields.StringField(choices=ROOF_MATERIAL_CHOICES) # Материал крыши
    # forest                          = mongo.fields.BooleanField(choices=FOREST_CHOICES) # Лес
    # pond                            = mongo.fields.BooleanField(choices=POND_CHOICES) # Водоем
    # apointment                      = mongo.fields.StringField(choices=APOINTMENT_CHOICES) # Назначение
    # percentage_of_readiness         = mongo.fields.DynamicField() # Процент готовности
    # outbildings                     = mongo.fields.BooleanField(choices=OUTBILDINGS_CHOICES) # Хоз постройки
    # garage                          = mongo.fields.BooleanField(choices=GARAGE_CHOICES) # Гараж
    # service_type                    = mongo.fields.StringField(choices=SERVICE_TYPE_CHOICES) # Тип услуги
    # property_type                   = mongo.fields.StringField(choices=PROPERTY_TYPE_CHOICES) # Тип недвижимости
    # parking_lot                     = mongo.fields.StringField(choices=PARKING_LOT_CHOICES) # Машиномест
    # light                           = mongo.fields.BooleanField(choices=LIGHT_CHOICES) # Свет
    # finish                          = mongo.fields.StringField(choices=FINISH_CHOICES) # Отделка
    # deadline                        = mongo.fields.StringField(choices=DEADLINE_CHOICES) # Срок сдачи
    # capacity_of_people              = mongo.fields.IntField(min_value=1, max_value=128) # Вместимость чел(макс)
    # parking_places                  = mongo.fields.IntField(min_value=1, max_value=128) # Мест для парковки
    # security                        = mongo.fields.BooleanField(choices=SECURITY_CHOICES) # Охрана
    # # TODO: Rewrite price_per_m2 field
    # price_per_m2                    = mongo.fields.StringField() # Цена за м2
    # prepaynment                     = mongo.fields.StringField(choices=PREPAYNMENT_CHOICES) # Предоплата
    # free_planning                   = mongo.fields.BooleanField(choices=FREE_PLANNING_CHOICES) # Свободная планировка
    # neighbors_in_the_apartment      = mongo.fields.StringField(choices=NEIGHBORS_IN_THE_APARTMENT_CHOICES) # Соседей в квартире
    # water                           = mongo.fields.BooleanField(choices=WATER_CHOICES) # Вода
    # youtube                         = mongo.fields.URLField() # 

    meta = {
            'indexes': [
                # {'fields': ['region'], 'unique': True, 'sparse': True, 'types': False },
                {'fields': ['region'] },
            ],
        }

    #TODO: make *_choice methods inherit from base. Or use decorator. DRY!
    #TODO: Make this methods more secure, cause data not validate in forms. 
    @classmethod
    def get_cat_tab_choices(self, group):
        from django.conf import settings
        cat_dict = settings.REALT_CAT_DICT
        cat_tr = settings.REALT_CAT_TR

        if group=="living":
            cat_dict_order = settings.REALT_CAT_DICT_ORDER_LIVING
        elif group=="commercial":
            cat_dict_order = settings.REALT_CAT_DICT_ORDER_COMMERCIAL

        out = []
        ordered_keys = sorted(cat_dict[group].keys(), key=lambda x: cat_dict_order[x])
        for k in ordered_keys:
            out.append((k, cat_tr[k]))
        out = tuple(out)
        return out

    @classmethod
    def get_cat_type_choices(self, group=None, tab=None):
        from django.conf import settings
        cat_dict = settings.REALT_CAT_DICT
        cat_tr = settings.REALT_CAT_TR

        if not group in cat_dict.keys() or not tab in cat_dict[group].keys():
            return ()

        out = []
        for k in cat_dict[group][tab]:
            out.append((k, cat_tr[k]))

        out = tuple(out)
        return out
        
        # return (('house', u"Дом"), ('room', u"Комната"), ('flat', u"Хата"))

    @classmethod
    def get_action_choices(self):
        from django.conf import settings
        act_dict = settings.REALT_ACTION_DICT

        out = []
        for k in act_dict:
            out.append((k, act_dict[k]))

        out = tuple(out)
        return out


    @classmethod
    def get_region_choices(cls):
        return ((x, x) for x in cls.objects.distinct('region'))    

    # using for tempalte rendering
    def get(self, key):
        return self[key]


    def clean111 (self):
        if not self.percentage_of_readiness ==None:
            msg_per_read = "percentage_of_readiness might be only int or long(> 6 chars) string"
            try:
                if not isinstance(int(self.percentage_of_readiness), int):
                    raise ValidationError(msg_per_read)
            except ValueError:
                raise ValidationError(msg_per_read)





class Currency(mongo.DynamicDocument):
    doc_id = mongo.fields.IntField()
    numcode = mongo.fields.IntField()
    rate = mongo.fields.DecimalField()
    scale = mongo.fields.IntField()


import sys
thismodule = sys.modules[__name__]
keys = filter(lambda x: x.endswith("_CHOICES"), locals().keys())
for k in keys:
    setattr(thismodule, k, tuple((x[1], x[1]) for x in getattr(thismodule, k)))
