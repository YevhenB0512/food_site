from django.utils.http import urlencode

from goods.models import Categories
from django import template


register = template.Library()


@register.simple_tag()
def categories_tag():
    return Categories.objects.all()[::-1]


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
