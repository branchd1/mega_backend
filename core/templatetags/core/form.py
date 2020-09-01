from django import template

register = template.Library()


@register.inclusion_tag('core/form_template.html', takes_context=True)
def form(context):
    return {
        'form': context['form']
    }
