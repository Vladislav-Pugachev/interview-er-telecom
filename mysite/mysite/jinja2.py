from django.templatetags.static import static
from django.urls import reverse
from django.contrib.humanize.templatetags.humanize import apnumber, intcomma, intword, naturalday, naturaltime, ordinal

from jinja2 import Environment

def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': static,
        'url': reverse,
    })
    env.filters.update({
        'apnumber': apnumber,
        'intcomma': intcomma,
        'intword': intword,
        'naturalday': naturalday,
        'naturaltime': naturaltime,
        'ordinal': ordinal,
    })
    return env