# -*- coding: utf8 -*-
# Create your views here.
from django import template
import logging

register = template.Library()


class EditHrefNode(template.Node):
    def __init__(self, href):
        self.href = href
    def render(self, context):
        return self.href

@register.tag(name="crud_href")
def crud_href(parser, userpk, profilepk, klass, baseurl):
    if userpk == profilepk:
        return EditHrefNode("<div class='edit-box'><a href='{% url %s_%baseurl profile.pk %}'>Добавить</a></div>" % (klass));
    else:
        return EditHrefNode("")

