from django import template

register = template.Library()

@register.filter(name='humanize_likes')
def humanize_likes(value):
    """ 1000 -> 1K """
    if isinstance(value, int):
        if value >= 1000:
            return str(value / 1000) + 'K'
        return value