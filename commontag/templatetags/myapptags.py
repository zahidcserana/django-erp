from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='button')
@stringfilter
def button(value):
    if value == 'back':
        return 'btn m-btn m-btn--gradient-from-info m-btn--gradient-to-warning'
    return 'btn m-btn m-btn--gradient-from-danger m-btn--gradient-to-warning'
