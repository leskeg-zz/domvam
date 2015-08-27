from django import forms

from models import Region, Ad, Attr, Object_type

class AttrForm(forms.ModelForm):
    class Meta:
        model = Attr