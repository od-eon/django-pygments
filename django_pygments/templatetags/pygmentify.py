from django import template
from django.template.defaultfilters import stringfilter
from django_pygments.utils import pygmentify_html
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
@stringfilter
def pygmentify(value):
    try:
        res = pygmentify_html(value)
    except Exception, e:
        print e
        print u'value="%s"' % value
        res = value
    return mark_safe(res)

@register.filter
@stringfilter
def pygmentify_inline(value):
    try:
        res = pygmentify_html(value, noclasses=True)
    except Exception, e:
        print e
        print u'value="%s"' % value
        res = value
    return mark_safe(res)

class PygmentifyNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        output = self.nodelist.render(context)
        try:
            res = pygmentify_html(output)
        except Exception, e:
            print e
            print u'value="%s"' % value
            res = output
        return mark_safe(res)

@register.tag
def pygment(parser, token):
    nodelist = parser.parse(('endpygment',))
    parser.delete_first_token()
    return PygmentifyNode(nodelist)

