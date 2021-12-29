'''
Relevant Django docs:
https://docs.djangoproject.com/en/<VAR:DJANGO_VERSION>/howto/custom-template-tags/
'''
from django import template


register = template.Library()

@register.filter
def lang_short_name(code):
    short_names = {
      'el': 'ΕΛ',
      'en': 'EN',
    }
    return short_names.get(code, '')
