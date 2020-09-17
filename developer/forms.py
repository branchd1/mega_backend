from django import forms

from core.models import Feature

from django.utils.translation import ugettext_lazy as _


class FeatureForm(forms.ModelForm):
    """ Form for creating and editing feature """
    class Meta:
        model = Feature
        fields = ['name', 'picture', 'description', 'payload']

        labels = {
            'name': _('feature name'),
            'picture': _('feature picture'),
            'description': _('description'),
            'payload': _('feature code')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label