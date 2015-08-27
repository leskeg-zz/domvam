# -*- coding: utf-8 -*-
from django import forms
# from django.forms.widgets import forms.TextInput, MultiWidget, HiddenInput
from django.forms.widgets import MultiWidget, HiddenInput

from captcha.fields import CaptchaField, CaptchaTextInput
from django.conf import settings
from form_widgets import *
from models import Advert, Region
from models import BALCONY_DECK_CHOICES, WALL_MATERIAL_CHOICES, WC_CHOICES, FLOORING_CHOICES, REPAIR_CHOICES, TYPE_OF_HOUSE_CHOICES, HEATING_CHOICES
from django.contrib.auth.models import User
from django.forms import ModelForm

REGIONS = (
    (0, "minsk"),
    (1, "gomel"),

)

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Имя пользователя'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
        }
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password'].required = True

class Filter(forms.Form):
    # region   = forms.CharField()
    region_ = forms.ChoiceField(
        choices=(('', ''),('', '')),
        widget=MultiChoicesHidden((StyleDropdown(attrs={}), HiddenInput)),
        required=False,
    )
    region__ = forms.ChoiceField(
        choices=(('', ''),('', '')),
        widget=MultiChoicesHidden((StyleDropdown(attrs={}), HiddenInput)),
        required=False,
    )
    
    currency = forms.ChoiceField(
        choices=(('usd', "USD"), ('eur', "EUR"), ('byr', "BYR")), 
        # widget=MultiChoicesHidden((StyleDropdown(attrs={"style": "width: 77px; float: right"}), HiddenInput))
        widget=MultiChoicesHidden((StyleDropdown(attrs={"style": "width: 77px; float: right"}), HiddenInput))
    )
    region = forms.ChoiceField(
        # choices=lambda: Advert.get_region_choices(),
        # choices=Advert.get_region_choices,
        # choices=((x, x) for x in Advert.objects.distinct('region')),
        choices=((x, x) for x in settings.MY_REGIONS),
        widget=MultiChoicesHidden((StyleDropdown(attrs={"style":"width:250px"}), HiddenInput)),
    )

    region2 = forms.ChoiceField(
        widget=MultiChoicesHidden((StyleDropdown(attrs={"style":"width:300px"}), HiddenInput)),
    )

    group    = forms.CharField()
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Поиск по названию"}))
    # cat_tab = forms.CharField()
    # action_type = forms.CharField()
    with_photo = forms.BooleanField(widget=StyleCheckbox, required=False)

    number_of_rooms = forms.ChoiceField(
        choices=(('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5+')), 
        widget=MultiChoicesHidden((StyleChooser(attrs={"style": "float: right;"}), HiddenInput))
    )
    
    price_min = forms.IntegerField(min_value=0)
    price_min.widget.attrs.update({'pattern': '[0-9]*'})
    price_max = forms.IntegerField(min_value=0)
    price_max.widget.attrs.update({'pattern': '[0-9]*'})

    total_area_min = forms.IntegerField(min_value=0)
    total_area_min.widget.attrs.update({'pattern': '[0-9]*'})
    total_area_max = forms.IntegerField(min_value=0)
    total_area_max.widget.attrs.update({'pattern': '[0-9]*'})

    living_area_min = forms.IntegerField(min_value=0)
    living_area_min.widget.attrs.update({'pattern': '[0-9]*'})
    living_area_max = forms.IntegerField(min_value=0)
    living_area_max.widget.attrs.update({'pattern': '[0-9]*'})

    kitchen_area_min = forms.IntegerField(min_value=0)
    kitchen_area_min.widget.attrs.update({'pattern': '[0-9]*'})
    kitchen_area_max = forms.IntegerField(min_value=0)
    kitchen_area_max.widget.attrs.update({'pattern': '[0-9]*'})

    floors_min = forms.IntegerField(min_value=0)
    floors_min.widget.attrs.update({'pattern': '[0-9]*'})
    floors_max = forms.IntegerField(min_value=0)
    floors_max.widget.attrs.update({'pattern': '[0-9]*'})

    plot_size_in_acros_min = forms.IntegerField(min_value=0)
    plot_size_in_acros_min.widget.attrs.update({'pattern': '[0-9]*'})
    plot_size_in_acros_max = forms.IntegerField(min_value=0)
    plot_size_in_acros_max.widget.attrs.update({'pattern': '[0-9]*'})

    # sort_order = forms.ChoiceField(
    #     choices=(
    #         ('-adding_date', u'Самые новые'),
    #         ('-price', u'Самые дорогие'),
    #         ('+price', u'Самые дешевые'),
    #         ('-title', u'А-Я'),
    #         ('+title', u'Я-А'),
    #         ('-images_len', u'Фотографии больше'),
    #         ('+images_len', u'Фотографии меньше'),
    #     ),
    #     widget=StyleSortOptions(attrs={"style": ""}),
    # )

    sort_order = forms.ChoiceField(
        choices=(
            ('adding_date', u'Дата добавления'),
            ('price', u'Цена'),
            ('title', u'Заголовок'),
            ('images_len', u'Фотографии'),
        ),
        widget=StyleSortOptions(attrs={"style": ""}),
    )
    # sort_order_direction = forms.ChoiceField(
    #     choices=(("+", "ASC"), ("-", "DESC")),
    #     widget=StyleSortOptionDirection,
    # )

    heating_type = forms.ChoiceField(
        choices=HEATING_CHOICES,
        widget=StyleDropdown(),
    )

    convert_currency_to = forms.ChoiceField(
        choices=(
            ("usd", "USD"),
            ("eur", "EUR"),
            ("byr", "BYR"),
        ),
        widget=StyleCurrency(
            attrs={
                "id": "currency", 
                "class": "sort-text", 
                "style": "vertical-align: top"
            }
        ),
    )

    icon_view = forms.ChoiceField(
        choices=(
            ("list-view", "big-icon"),
            ("grill-view", "small-icon"),
        ),
        widget=StyleView(),
    )

    water = forms.ChoiceField(
            widget=StyleSwitch,
            choices=(('yes', u'Есть'), ('no', u'Не важно')),
    )

    garage = forms.ChoiceField(
            widget=StyleSwitch,
            choices=(('yes', u'Есть'), ('no', u'Не важно'))
    )
    heating = forms.ChoiceField(
            widget=StyleSwitch,
            choices=(('yes', u'Есть'), ('no', u'Не важно'))
    )
    sewerage = forms.ChoiceField(
            widget=StyleSwitch,
            choices=(('yes', u'Есть'), ('no', u'Не важно'))
    )
    demolition = forms.ChoiceField(
            widget=StyleSwitch,
            choices=(('yes', u'Есть'), ('no', u'Не важно'))
    )

    electricity = forms.ChoiceField(
            widget=StyleSwitch,
            choices=(('yes', u'Есть'), ('no', u'Не важно'))
    )

    mortgage = forms.ChoiceField(
            widget=StyleSwitch,
            choices=(('yes', u'Есть'), ('no', u'Не важно'))
    )

    # action_type = forms.ChoiceField(
    #     widget=StyleSwitch,
    #     choices=(('sale', u'Продажа'),('rent', u'Аренда'))
    # )
    action_type = forms.ChoiceField(
        choices=(('sale', u"Продажа"), ('rent', u"Аренда")),
        widget=MultiChoicesHidden((StyleSwitch, HiddenInput)),
        required=True,
        # initial='living',
    )

    number_of_rooms = forms.ChoiceField(
        choices=(('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5+')), 
        widget=MultiChoicesHidden((StyleChooser(), HiddenInput))
    )

    month = forms.BooleanField(widget=StyleCheckbox(label = u"Длительная"), required=False)
    day = forms.BooleanField(widget=StyleCheckbox(label = u"По суткам"), required=False)
    exchange = forms.BooleanField(widget=StyleCheckbox(label = u"Обмен"), required=False)
    with_photo = forms.BooleanField(widget=StyleCheckbox(label = u"С фото"), required=False)
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Поиск по названию", "style":"width:300px"}))

    def __init__(self, *args, **kwargs):
        super(Filter, self).__init__(*args, **kwargs)
        self.fields['cat_tab'] = forms.ChoiceField(
            choices=Advert.get_cat_tab_choices(self.data['group']))
        
        self.fields['cat_type'] = forms.ChoiceField(
            widget=StyleDropdown, 
            choices=Advert.get_cat_type_choices(
                self.data['group'], self.data['cat_tab']
            )
        )
        # self.fields['action_type'] = forms.ChoiceField(
        #     widget=StyleSwitch,
        #     choices=Advert.get_action_choices()
        #     # choices=(('rent', u'Аренда'), ('sale', u'Продажа'), ('exchange', u'Обмен'))
        # )

        

        for field_name, obj in self.fields.iteritems():
            self.fields[field_name].required = False

class TicketForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 500px; height: 34px","placeholder": "Имя"}),required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={"style": "width: 500px; height: 34px","placeholder": "E-mail"}),required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 500px; height: 34px","mask": "+999 99 999 99 99", "placeholder": "Телефон"}),required=True)
    text = forms.CharField(widget=forms.Textarea(attrs={"style": "width: 500px; height: 200px","placeholder": ""}),required=True)

class AgencyForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 354px; height: 34px","placeholder": "Имя"}),required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={"style": "width: 354px; height: 34px","placeholder": "E-mail"}),required=True)
    password = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 354px; height: 34px","placeholder": "Пароль"}),required=True)
    name_of_entity = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 354px; height: 34px","placeholder": "Наименование юридического лица", 'required':'required'}), required=True)
    head_name = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 354px; height: 34px","placeholder": "ФИО руководителя", 'required':'required'}),required=True)
    head_position = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 354px; height: 34px","placeholder": "Должность руководителя", 'required':'required'}),required=True)
    country = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 354px; height: 34px","placeholder": "Страна", 'required':'required'}),required=True)
    locality = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 354px; height: 34px","placeholder": "Населенный пункт", 'required':'required'}),required=True)
    region = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 354px; height: 34px","placeholder": "Область, район", 'required':'required'}),required=False)
    post_code = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 354px; height: 34px","placeholder": "Индекс", 'required':'required'}),required=True)
    street = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 354px; height: 34px","placeholder": "Улица", 'required':'required'}),required=True)
    house_number_body = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 354px; height: 34px","placeholder": "№ Дома-корпус", 'required':'required'}),required=False)
    office_number_room_apartment = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 354px; height: 34px","placeholder": "№ Офиса, комнаты или квартиры", 'required':'required'}),required=False)
    mail_adress = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 354px; height: 34px","placeholder": "Адрес для почтовых отправлений", 'required':'required'}),required=False)
    contact_phone = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 354px; height: 34px","mask": "+999 99 999 99 99", "placeholder": "Контактный телефон", 'required':'required'}),required=True)
    mobile_phone = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 354px; height: 34px","mask": "+999 99 999 99 99", "placeholder": "Мобильный телефон"}),required=False)
    fax = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 354px; height: 34px","mask": "+999 99 999 99 99", "placeholder": "Факс"}),required=False)
    extra_email = forms.CharField(widget=forms.EmailInput(attrs={"style": "width: 354px; height: 34px","placeholder": "Дополнительный E-mail"}),required=False)
    UNP_organization = forms.CharField(widget=forms.NumberInput(attrs={"style": "width: 354px; height: 34px","placeholder": u"УНП вашей организации", 'required':'required'}),required=True)
    registering_autority = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 354px; height: 34px","placeholder": "Орган осуществивший регистрацию", 'required':'required'}),required=True)
    number_state_registration = forms.CharField(widget=forms.NumberInput(attrs={"style": "width: 354px; height: 34px","placeholder": u"№ решения о государственной регистрации"}),required=False)
    date_state_registration = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 354px; height: 34px","placeholder": "Дата государственной регистрации (DD-MM-YY)", 'required':'required'}),required=True)

# Rewrite Form to use any kind of MVVM (knockout, angular, etc...)
# class AddCard(Filter):
class AddCard(forms.Form):
    # location = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 350px; height: 34px", "placeholder": "Город/Поселок"}),required=False)
    security = forms.BooleanField(widget=StyleCheckbox(label = u"Охрана"), required=False)
    prepayment = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": u"Предоплата"}),required=False)
    # prescribed_persons = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": u"Прописано человек"}))
    for_students = forms.BooleanField(widget=StyleCheckbox(label = u"Для студентов"), required=False)
    # agency = forms.BooleanField(widget=StyleCheckbox(label = u"Агентство"), required=False)
    double_glazed_windows = forms.BooleanField(widget=StyleCheckbox(label = u"Стеклопакеты"), required=False)
    rent = forms.BooleanField(widget=StyleCheckbox(label = u"Посуточно"), required=False)
    finish = forms.BooleanField(widget=StyleCheckbox(label = u"Отделка"), required=False)
    city_phone = forms.BooleanField(widget=StyleCheckbox(label = u"Городской телефон"), required=False)
    lift = forms.BooleanField(widget=StyleCheckbox(label = u"Лифт"), required=False)
    kids = forms.BooleanField(widget=StyleCheckbox(label = u"Дети"), required=False)
    pets = forms.BooleanField(widget=StyleCheckbox(label = u"Домашние животные"), required=False)
    # title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": u"Заголовок"}))
    neighbors_in_the_apartment = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": u"Соседей в квартире"}),required=False)
    # land_area = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": u"Площадь участка"}))
    area = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": u"Район"}),required=False)
    plot_size_in_acros = forms.FloatField(widget=forms.NumberInput(attrs={"style": "width: 354px; height: 34px", "placeholder": "Площадь участка в сотках"}),required=False)
    households_built = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": u"Хоз постройки"}),required=False)
    fence = forms.BooleanField(widget=StyleCheckbox(label = u"Забор"), required=False)
    column = forms.BooleanField(widget=StyleCheckbox(label = u"Колонка"), required=False)
    cellar = forms.BooleanField(widget=StyleCheckbox(label = u"Погреб"), required=False)
    # heating = forms.BooleanField(widget=StyleCheckbox(label = u"Отопление"), required=False)
    heating = forms.ChoiceField(widget=MultiChoicesHidden((StyleDropdown(attrs={"style": "width: 354px; height: 34px"}), HiddenInput)), choices=HEATING_CHOICES,required=False)
    garage = forms.BooleanField(widget=StyleCheckbox(label = u"Гараж"), required=False)
    parking_places = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Машиномест"}))
    km_from_city = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": u"Км от города"}),required=False)
    loft = forms.BooleanField(widget=StyleCheckbox(label = u"Чердак"), required=False)
    bathroom = forms.BooleanField(widget=StyleCheckbox(label = u"Санузел"), required=False)
    sewerage = forms.BooleanField(widget=StyleCheckbox(label = u"Канализация"), required=False)
    # km_from_city = forms.IntegerField(widget=forms.NumberInput(attrs={"style": "width: 265px; height: 34px", "placeholder": u"km_from_city"}))
    # price_per_m2 = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": u"Колво кв.м."}))
    light = forms.BooleanField(widget=StyleCheckbox(label = u"Освещение"), required=False)
    # ownership = forms.BooleanField(widget=StyleCheckbox(label = u"Собственность"), required=False)
    # percentage_of_readiness = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": u"Процент готовности"}))
    electricity = forms.BooleanField(widget=StyleCheckbox(label = u"Электричество"), required=False)
    gas = forms.BooleanField(widget=StyleCheckbox(label = u"Газ"), required=False)
    balcony_built = forms.BooleanField(widget=StyleCheckbox(label = u"Хоз постройки"), required=False)
    exchange_description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "exchange_description"}),required=False)


    group = forms.ChoiceField(
        choices=(('living', u"Жилая"), ('commercial', u"Коммерческая")),
        widget=MultiChoicesHidden((StyleSwitch, HiddenInput)),
        required=True,
        # initial='living',
    )

    # action_type = forms.ChoiceField(
    #     choices=(('sale', u"Продажа"), ('rent', u"Аренда")),
    #     widget=MultiChoicesHidden((StyleSwitch, HiddenInput)),
    #     required=True,
    #     # initial='living',
    # )
    contact_name = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 200px; height: 34px", "placeholder": "Контактное лицо"}),required=True)
    action_type = forms.CharField(widget=forms.TextInput(attrs={"type": "hidden"}))

    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Текст обьявления"}))
    
    region = forms.ChoiceField(
        # choices=Region.get_choices(),
        choices=((x, x) for x in settings.MY_REGIONS),
        widget=MultiChoicesHidden((StyleDropdown, HiddenInput)),
        required=False,
    )
    region_ = forms.ChoiceField(
        choices=(('', ''),('', '')),
        widget=MultiChoicesHidden((StyleDropdown(attrs={}), HiddenInput)),
        required=False,
    )
    region__ = forms.ChoiceField(
        choices=(('', ''),('', '')),
        widget=MultiChoicesHidden((StyleDropdown(attrs={}), HiddenInput)),
        required=False,
    )
    region2 = forms.CharField(widget=forms.TextInput(attrs={}),required=False)
    # microregion = forms.CharField(widget=forms.TextInput(attrs={"placeholder": u"Микрорайон"}),required=False)

    # city = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Город"}),required=False)
    address = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Улица"}))
    obl = forms.CharField(widget=forms.TextInput(),required=True)
    name = forms.CharField(widget=forms.TextInput(),required=True)
    raion = forms.CharField(widget=forms.TextInput(),required=False)
    house = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Дом"}))

    price = forms.IntegerField(widget=forms.NumberInput(attrs={"style": "width: 265px; height: 34px", "placeholder": u"Цена"}))
    # currency = forms.ChoiceField(choices=(('usd', "USD"), ('eur', "EUR"), ('byr', "BYR")), widget=StyleDropdown(attrs={"style": "width: 77px; float: right"}))
    currency = forms.ChoiceField(
        choices=(('usd', "USD"), ('eur', "EUR"), ('byr', "BYR")), 
        # widget=MultiChoicesHidden((StyleDropdown(attrs={"style": "width: 77px; float: right"}), HiddenInput))
        widget=MultiChoicesHidden((StyleDropdown(attrs={"style": "width: 77px; float: right"}), HiddenInput))
    )

    year_built = forms.IntegerField(widget=forms.NumberInput(attrs={"style": "width: 354px; height: 34px", "placeholder": u"Год постройки"}),required=False)

    floor = forms.IntegerField(widget=forms.NumberInput(attrs={"style": "width: 354px; height: 34px", "placeholder": u"Этаж"}),required=False)
    number_of_rooms = forms.ChoiceField(
        choices=(('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5+')), 
        widget=MultiChoicesHidden((StyleChooser(attrs={"style": "float: right;"}), HiddenInput)),
        required=False
    )
    number_of_floors = forms.IntegerField(widget=forms.NumberInput(attrs={"style": "width: 354px; height: 34px","placeholder": u"Этажность"}),required=False)

    kitchen_area = forms.FloatField(widget=forms.NumberInput(attrs={"style": "width: 354px; height: 34px", "placeholder": "Площадь кухни"}),required=False)
    total_area = forms.FloatField(widget=forms.NumberInput(attrs={"style": "width: 354px; height: 34px", "placeholder": "Площадь участка"}),required=False)
    living_area = forms.FloatField(widget=forms.NumberInput(attrs={"style": "width: 354px; height: 34px", "placeholder": "Жилая площадь"}),required=False)

    balcony_deck = forms.ChoiceField(widget=MultiChoicesHidden((StyleDropdown(attrs={"style": "width: 354px; height: 34px"}), HiddenInput)), choices=BALCONY_DECK_CHOICES, required=False)
    wall_material = forms.ChoiceField(widget=MultiChoicesHidden((StyleDropdown(attrs={"style": "width: 354px; height: 34px"}), HiddenInput)), choices=WALL_MATERIAL_CHOICES, required=False)
    wc = forms.ChoiceField(widget=MultiChoicesHidden((StyleDropdown(attrs={"style": "width: 354px; height: 34px"}), HiddenInput)), choices=WC_CHOICES,required=False)
    flooring = forms.ChoiceField(widget=MultiChoicesHidden((StyleDropdown(attrs={"style": "width: 354px; height: 34px"}), HiddenInput)), choices=FLOORING_CHOICES,required=False)
    repair = forms.ChoiceField(widget=MultiChoicesHidden((StyleDropdown(attrs={"style": "width: 354px; height: 34px"}), HiddenInput)), choices=REPAIR_CHOICES,required=False)
    # type_of_house = forms.ChoiceField(widget=MultiChoicesHidden((StyleDropdown(attrs={"style": "width: 354px; height: 34px"}), HiddenInput)), choices=TYPE_OF_HOUSE_CHOICES)

    #chute = forms.BooleanField(widget=StyleCheckbox)
    internet = forms.BooleanField(widget=StyleCheckbox(label = u"Интернет"), required=False)
    home_appliances = forms.BooleanField(widget=StyleCheckbox(label = u"Бытовая техника"), required=False)
    furniture = forms.BooleanField(widget=StyleCheckbox(label = u"Мебель"), required=False)
    agreement = forms.BooleanField(widget=StyleCheckbox(label = u"Я согласен с "), required=True)
    auction = forms.BooleanField(widget=StyleCheckbox(label = u"Возможен торг"), required=False)
    # period = forms.BooleanField(widget=StyleCheckbox(label = u"Интернет"), required=False)
    # captcha = CaptchaField(widget=StyleCaptchaTextInput(), required=True)
    # captcha = CaptchaField()

    # name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Ваше имя"}))
    # email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "E-mail"}))
    phones = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 200px; height: 34px", "mask": "+999 99 999 99 99", "placeholder": "Телефон"}),required=True)
    phones2 = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 200px; height: 34px", "mask": "+999 99 999 99 99", "placeholder": "Телефон"}),required=False)
    phones3 = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 200px; height: 34px", "mask": "+999 99 999 99 99", "placeholder": "Телефон"}),required=False)
    month = forms.BooleanField(widget=StyleCheckbox(label = u"Длительная"), required=False)
    day = forms.BooleanField(widget=StyleCheckbox(label = u"По суткам"), required=False)
    exchange = forms.BooleanField(widget=StyleCheckbox(label = u"Обмен"), required=False)
    # wrapper for convert group_0 group_1 to group dict keys
    # Todo: raise if more than 1 key with eq name
    @property
    def data2(self):
        out = self.data.copy()
        cor_dict = {}
        process_keys = ('group', 'cat_tab', 'cat_type', 'currency')
        affected_keys = filter(lambda x: x.startswith(process_keys), self.data.keys())

        for x in affected_keys:
            _clean = x.rsplit("_", 1)[0]
            # cor_dict[_clean] = x
            cor_dict[x] = _clean
            out[_clean] = out[x]
            del out[x]

        return out


    def __init__(self, *args, **kwargs):
        super(AddCard, self).__init__(*args, **kwargs)

        if "group" in self.data2.keys() and not self.data2['group'] == '':
            cat_tab_choices = Advert.get_cat_tab_choices(self.data2['group'])
            if "cat_tab" in self.data2.keys():
                cat_type_choices = Advert.get_cat_type_choices(
                    self.data2['group'], self.data2['cat_tab']
                )
            else:
                cat_type_choices = ()

        else:
            cat_tab_choices = ()
            cat_type_choices = ()

        self.fields['cat_tab'] = forms.ChoiceField(
            choices=cat_tab_choices,
            # widget=StyleDropdown(value='flat'),
            widget=MultiChoicesHidden((StyleDropdown, HiddenInput)),
        )
        self.fields['cat_type'] = forms.ChoiceField(
            choices=cat_type_choices,
            # widget=StyleDropdown, 
            widget=MultiChoicesHidden((StyleDropdown, HiddenInput)),
        )

        # for field_name, obj in self.fields.iteritems():
        #     self.fields[field_name].required = False

        self.fields['cat_tab'].required = True
        self.fields['cat_type'].required = True
        for field in ['balcony_deck','house','neighbors_in_the_apartment','parking_places','wall_material','year_built','flooring']:
            self.fields[field].required = False

class Card(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Текст комментария"}))

class AddCardRentFlat(AddCard):
    def __init__(self, *args, **kwargs):
        super(AddCard, self).__init__(*args, **kwargs)
        exclude = [
            'neighbors_in_the_apartment',
            # 'land_area',
            'area',
            'households_built',
            'fence',
            'column',
            'cellar',
            'heating',
            'garage',
            'parking_places',
            'km_from_city',
            'loft',
            'bathroom',
            'sewerage',
            # 'price_per_m2',
            'light',
            # 'ownership',
            # 'percentage_of_readiness',
            'electricity',
            'gas',
            'balcony_built',
            'kitchen_area',
            'region',
            'region_',
            'region__',
            'region2',
            ]

        for x in exclude:
            del self.fields[x]

class AddCardRentRoom(AddCard):
    def __init__(self, *args, **kwargs):
        super(AddCard, self).__init__(*args, **kwargs)
        exclude = [
            'area',
            'households_built',
            'kitchen_area',
            'km_from_city',
            # 'land_area',
            'living_area',
            # 'percentage_of_readiness',
            # 'price_per_m2',
            'total_area',
            'parking_places',
            'region',
            'region_',
            'region__',
            'region2',
            ]

        for x in exclude:
            del self.fields[x]

class AddCardRentHouse(AddCard):
    def __init__(self, *args, **kwargs):
        super(AddCard, self).__init__(*args, **kwargs)
        exclude = [
            'floor',
            'kitchen_area',
            'neighbors_in_the_apartment',
            'number_of_floors',
            # 'percentage_of_readiness',
            # 'price_per_m2',
            'wall_material',
            'wc',
            'year_built',
            'parking_places',
            'area',
            'region',
            'region_',
            'region__',
            'region2',
            ]

        for x in exclude:
            del self.fields[x]

class AddCardRentArea(AddCard):
    def __init__(self, *args, **kwargs):
        super(AddCard, self).__init__(*args, **kwargs)
        exclude = [
            'kitchen_area',
            'number_of_rooms',
            'year_built',
            'flooring',
            # 'prescribed_persons',
            'area',
            # 'percentage_of_readiness',
            'floor',
            'repair',
            # 'land_area',
            'balcony_deck',
            'neighbors_in_the_apartment',
            # 'type_of_house',
            'wall_material',
            'number_of_floors',
            'living_area',
            # 'microregion',
            'parking_places',
            'region',
            'region_',
            'region__',
            'region2',
            ]

        for x in exclude:
            del self.fields[x]

class AddCardSaleFlat(AddCard):
    def __init__(self, *args, **kwargs):
        super(AddCard, self).__init__(*args, **kwargs)
        exclude = [
            'area',
            'households_built',
            'km_from_city',
            # 'land_area',
            'neighbors_in_the_apartment',
            'prepayment',
            # 'price_per_m2',
            'parking_places',
            'region',
            'region_',
            'region__',
            'region2',
            ]

        for x in exclude:
            del self.fields[x]

class AddCardSaleHouse(AddCard):
    def __init__(self, *args, **kwargs):
        super(AddCard, self).__init__(*args, **kwargs)
        exclude = [
            'floor',
            'households_built',
            'kitchen_area',
            'neighbors_in_the_apartment',
            # 'percentage_of_readiness',
            'prepayment',
            # 'prescribed_persons',
            # 'price_per_m2',
            'wc',
            'year_built',
            'parking_places',
            'area',
            'region',
            'region_',
            'region__',
            'region2',
            ]

        for x in exclude:
            del self.fields[x]

class AddCardSaleArea(AddCard):
    def __init__(self, *args, **kwargs):
        super(AddCard, self).__init__(*args, **kwargs)
        exclude = [
            'area',
            'balcony_deck',
            'floor',
            'flooring',
            'kitchen_area',
            # 'land_area',
            'living_area',
            # 'microregion',
            'neighbors_in_the_apartment',
            'number_of_floors',
            'number_of_rooms',
            # 'percentage_of_readiness',
            'prepayment',
            # 'prescribed_persons',
            'repair',
            # 'type_of_house',
            'wall_material',
            'year_built',
            'parking_places',
            'region',
            'region_',
            'region__',
            'region2',
            ]

        for x in exclude:
            del self.fields[x]

class AddCardCommercial(AddCard):
    def __init__(self, *args, **kwargs):
        super(AddCard, self).__init__(*args, **kwargs)
        exclude = [
            'kitchen_area',
            'number_of_rooms',
            'year_built',
            'flooring',
            # 'prescribed_persons',
            'area',
            # 'percentage_of_readiness',
            'floor',
            'repair',
            # 'land_area',
            'balcony_deck',
            'neighbors_in_the_apartment',
            # 'type_of_house',
            'wall_material',
            'number_of_floors',
            'living_area',
            # 'microregion',
            'parking_places',
            'households_built',
            'prepayment',
            'km_from_city',
            'plot_size_in_acros',
            'region',
            'region_',
            'region__',
            'region2',
            ]

        for x in exclude:
            del self.fields[x]
    
