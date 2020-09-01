from django import template

register = template.Library()


@register.inclusion_tag('core/form_template.html', takes_context=True)
def form(context, is_multipart=False):
    return {
        'form': context['form'],
        'is_multipart': is_multipart
    }