""" This module contains the form template tag """

from django import template

register = template.Library()


@register.inclusion_tag('core/form_template.html', takes_context=True)
def form(context, is_multipart=False):
    """
    form template tag

    Parameters
    ----------
    context
    is_multipart : bool
        True if the form enc-type is multipart, False otherwise

    Returns
    -------
    dict
        Dictionary containing the parent template context and data indicating if the form is multipart or not

    """
    return {
        'form': context['form'],
        'is_multipart': is_multipart
    }