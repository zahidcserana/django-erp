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
    if value == 'menu_help':
        return 'm-menu__link-icon flaticon-info'
    if value == 'menu_technology':
        return 'm-menu__link-icon flaticon-technology'
    if value == 'menu_sales':
        return 'm-menu__link-icon flaticon-clipboard'
    if value == 'menu_suitcase':
        return 'm-menu__link-icon flaticon-suitcase'
    if value == 'menu_graphic':
        return 'm-menu__link-icon flaticon-graphic'

    return 'btn m-btn m-btn--gradient-from-danger m-btn--gradient-to-warning'


@register.filter(name='status_class')
@stringfilter
def status_class(value):
    if value == 'ACTIVE':
        return 'm-badge m-badge--success m-badge--wide'
    if value == 'INACTIVE':
        return 'm-badge m-badge--danger m-badge--wide'
    if value == 'IN_PROGRESS':
        return 'm-badge m-badge--info m-badge--wide'
    if value == 'COMPLETE':
        return 'm-badge m-badge--warning m-badge--wide'


@register.filter(name='status_task')
def status_task():
    Statuses = {
        'ACTIVE': 'Active',
        'HOLD': 'Hold',
        'IN_PROGRESS': 'In Progress',
        'COMPLETE': 'Complete',
        'ARCHIVE': 'archive',
        'INACTIVE': 'Inactive'
    }
    return Statuses
