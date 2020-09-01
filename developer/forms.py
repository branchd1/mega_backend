from django import forms

from core.models import Feature

from django.utils.translation import ugettext_lazy as _


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ['name', 'picture', 'community_type', 'description', 'payload']

        labels = {
            'name': _('feature name'),
            'picture': _('feature picture'),
            'community_type': _('community type'),
            'description': _('description'),
            'payload': _('feature code')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label