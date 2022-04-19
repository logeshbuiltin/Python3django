from django import template

register = template.Library()

@register.filter
def do_subtract(value, arg):
    return round(value - arg, 2)