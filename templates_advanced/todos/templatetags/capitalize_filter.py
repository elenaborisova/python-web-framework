from django import template

register = template.Library()


@register.filter()
def capitalize(value, chars_count=1):
    return value[:chars_count].upper() + value[chars_count+1:].lower()
