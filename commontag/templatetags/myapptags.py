from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='button_class')
@stringfilter
def button_class(value):
    if value == 'back':
        return 'btn m-btn m-btn--gradient-from-info m-btn--gradient-to-warning'
    if value == 'edit':
        return 'btn btn-success m-btn m-btn--icon btn-sm m-btn--icon-only'
    if value == 'delete':
        return 'btn btn-danger m-btn m-btn--icon btn-sm m-btn--icon-only'
    return 'btn m-btn m-btn--gradient-from-danger m-btn--gradient-to-warning'


@register.filter(name='status_class')
@stringfilter
def status_class(value):
    if value == 'ACTIVE':
        return 'm-badge m-badge--success m-badge--wide'
    if value == 'INACTIVE':
        return 'm-badge m-badge--warning m-badge--wide'
