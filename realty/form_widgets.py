# -*- coding: utf-8 -*-

from itertools import chain

from django.utils.safestring import mark_safe
from django.forms.util import flatatt
from django.utils.html import format_html
from django.utils.encoding import force_text
from django.forms import Widget, Select, CheckboxInput
from django.forms.widgets import boolean_check, TextInput, MultiWidget, HiddenInput
from captcha.fields import CaptchaTextInput, BaseCaptchaTextInput

class MultiChoicesHidden(MultiWidget):
    def __init__(self, widgets, attrs=None):
        self.widgets = [w() if isinstance(w, type) else w for w in widgets]
        self.attrs = {}
        # super(MultiChoicesHidden, self).__init__(attrs)

    @property
    def choices(self):
        return self.widgets[0].choices
    @choices.setter
    def choices(self, value):
        # [0] - StyleSwitch(Select)
        self.widgets[0].choices = value

    def decompress(self, value):
        if value:
            if isinstance(value, list):
                out = [x for x in value if x is not None]
                if len(out) == 1:
                    return [None, out[1]] # TODO: fix for right pick
                else:
                    return [None, None]
            else:
                return [None, value]
        return [None, None]

    def value_from_datadict(self, data, files, name):
        style  = self.widgets[0].value_from_datadict(data, files, name + '_0')
        hidden = self.widgets[1].value_from_datadict(data, files, name + '_1')

        if style and not hidden:
            #ajax request
            return style
        elif not style and hidden:
            # regular form POST
            return hidden
        elif not style and not hidden:
            # unbound form
            return None

    def format_output(self, rendered_widgets):
        return ''.join(rendered_widgets)

class StyleDropdown(Select):
    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        final_attrs['class'] = "select-wrap"

        options, selected = self.render_options(choices, [value])
        output = [format_html(u'<div{0}><div class="select" id="{2}_id" data-type="{2}"><span>{1}</span></div>', flatatt(final_attrs), selected, name)]
        output.append("<ul>")
        if options:
            output.append(options)
        output.append("</ul>")
        output.append('</div>')
        return mark_safe('\n'.join(output))

    def render_option(self, selected_choices, option_value, option_label):
        option_value = force_text(option_value)
        # if option_value in selected_choices:
        #     selected_html = mark_safe(' selected="selected"')
        #     if not self.allow_multiple_selected:
        #         # Only allow for a single selection.
        #         # selected_choices.remove(option_value)
        # else:
        #     selected_html = ''
        return format_html(u'<li class="option" data-value="{0}">{1}</li>',
                           unicode(option_value),
                           # unicode(selected_html),
                           force_text(unicode(option_label)))

    def render_options(self, choices, selected_choices):
        # Normalize to strings.
        selected_choices = set(force_text(v) for v in selected_choices)
        output = []
        _values_dict = {}
        for option_value, option_label in chain(self.choices, choices):
            if isinstance(option_label, (list, tuple)):
                raise ValueError("list or tuple nested not supported")
            else:
                output.append(self.render_option(selected_choices, option_value, option_label))
                _values_dict[option_value] = option_label

        if len(list(selected_choices)[0]) == 0 or len(_values_dict.keys()) == 0:
            selected_choices = ""

        else:
            try:
                selected_choices = _values_dict[list(selected_choices)[0]]
            except KeyError:
                selected_choices = ""

        return '\n'.join(output), selected_choices


class StyleSwitch(Select):
    # @property
    # def choices(self):
    #     return self._choices
    # @choices.setter
    # def choices(self, value):
    #     self._choices = value

    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = ''
        # output = [format_html(u'<div id="sell-rent-switch">')]
        output = []
        for option_value, option_label in chain(self.choices, choices):
            
            _active_str = ''
            if value == option_value:
                _active_str = " active "
            output.append(format_html(u'<div class="{2}" id="{3}_{0}" data-type="{3}" data-value="{0}">{1}</div>', option_value, option_label, _active_str, name))
        # output.append("</div>")
        return mark_safe('\n'.join(output))


class StyleChooser(Select):
    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        if "class" in final_attrs.keys():
            final_attrs['class'] = "%s %s" % (final_attrs['class'], "button-chooser")
        else:
            final_attrs['class'] = "button-chooser"
            
        output = [format_html(u"<div{0}>", flatatt(final_attrs))]
        for option_value, option_label in chain(self.choices, choices):
            _active_str = ""
            if value == option_value:
                _active_str = " showR "
            output.append(format_html(u'<buttons class="room" data-type="{0}" data-value="{1}">{2}</buttons>', name, option_value, option_label, _active_str))

        output.append(u'</div>')
        return mark_safe('\n'.join(output))

class StyleCurrency(Select):
    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        final_attrs['data-type'] = name
        output = [format_html(u'<div{0}>Валюта:', flatatt(final_attrs))]
        for option_value, option_label in chain(self.choices, choices):
            _active_str = ''
            if value == option_value:
                _active_str = ' active '
            output.append(format_html(u'<span class="{0}" data-value="{1}">{2}</span>', _active_str, option_value, option_label))

        output.append(u'</div>')
        return mark_safe('\n'.join(output))

class StyleView(Select):
    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = ''
        #final_attrs = self.build_attrs(attrs, name=name)
        #final_attrs['data-type'] = name
        #output = [format_html(u'<div{0}>', flatatt(final_attrs))]
        output = []
        for option_value, option_label in chain(self.choices, choices):
            _active_str = ''
            if value == option_value:
                _active_str = ' active '
            output.append(format_html(u'<div id="{2}" class="filter-link {0}" data-type="{3}" data-value={1}><div id="inner-{2}" class="{0}"></div></div>', _active_str, option_value, option_label, name))

            #<div id="big-icon" class="filter-link" data-type="icon_view" data-value="list-view"><div id="inner-big-icon"></div></div>
        
        #output.append(u'</div>')
        return mark_safe('\n'.join(output))

class StyleSortOptions(Select):
    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = ''
        output = []
        for option_value, option_label in chain(self.choices, choices):
            output.append(format_html(u'<span><span class="sort-kind">{1}</span><span class="sort-direction" data-type="{2}" data-value="+{0}" style="cursor:pointer">&#9650</span><span class="sort-direction" data-type="{2}" data-value="-{0}" style="cursor:pointer">&#9660</span></span>', option_value, option_label, name))

        return mark_safe('\n'.join(output))

class StyleCheckbox(CheckboxInput):
    def __init__(self, attrs=None, check_test=None, label=""):
        super(CheckboxInput, self).__init__(attrs)
        # check_test is a callable that takes a value and returns True
        # if the checkbox should be checked for that value.
        self.check_test = boolean_check if check_test is None else check_test
        self.label = label
  

    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, type='checkbox', name=name)
        if self.check_test(value):
            final_attrs['checked'] = 'checked'
        if not (value is True or value is False or value is None or value == ''):
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(value)
        # return format_html('<input{0} />', flatatt(final_attrs))
        return format_html(u'<label><span style="cursor:pointer"><div class="checkbox"><input {0}></div>{1}</span></label>', flatatt(final_attrs), self.label)

class MyBaseCaptchaTextInput(BaseCaptchaTextInput, MultiWidget):
    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        widgets = (
            HiddenInput(attrs),
            TextInput(attrs.update({
                "style": "width: 354px;height: 34px;vertical-align: middle;"
            })),
        )
        super(BaseCaptchaTextInput, self).__init__(widgets, attrs)

class StyleCaptchaTextInput(CaptchaTextInput, MyBaseCaptchaTextInput):
    def render(self, name, value, attrs=None):
        self.fetch_captcha_store(name, value, attrs)

        self.image_and_audio = '<img src="%s" alt="captcha" class="captcha" />' % self.image_url()

        return super(CaptchaTextInput, self).render(name, self._value, attrs=attrs)
