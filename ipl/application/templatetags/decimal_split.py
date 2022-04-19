from django import template

register = template.Library()

@register.filter
def decimal_split(value):
    return str(value).split('.')