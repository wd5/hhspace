# -*- coding: utf8 -*-
from django.core.urlresolvers import reverse

def edit_url(user, profile, baseurl, args = [], withhtml=1):
    klass = profile.__class__.__name__.lower()

    if user.__class__.__name__.lower() == 'anonymoususer':
        return ''
    
    html = "<div class='edit-box'><a href='%s'>Добавить</a></div>"

    if klass == 'group' and [int(x) for x in profile.leaders.split(",")].__contains__(user.pk):
        url = reverse("%s_%s"% (klass, baseurl), args=args)
        if withhtml:
            return html % url
        else:
            return url

    if klass == "singer" and user.pk == profile.pk:
        url = reverse("%s_%s"% (klass, baseurl), args=args)
        if withhtml:
            return html % url
        else:
            return url
        
    if klass == "customuser" and user.pk == profile.pk:
        url = reverse("%s_%s"% (klass, baseurl), args=args)
        if withhtml:
            return html % url
        else:
            return url

    return ''
