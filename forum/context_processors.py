# -*- coding: utf-8 -*-
from .models import NodeGroup
from django.utils.translation import ugettext as _
from django.conf import settings


def forum_processor(request):
    node_groups = NodeGroup.objects.all()
    site_name = _(getattr(settings, 'forum_SITE_NAME', ''))
    forum_login_url_name = getattr(settings, 'forum_LOGIN_URL_NAME', 'forum:login')
    forum_reg_url_name = getattr(settings, 'forum_REG_URL_NAME', 'forum:reg')
    try:
        unread_count = request.user.received_notifications.filter(read=False).count()
    except AttributeError:
        unread_count = None
    return {
        'node_groups': node_groups,
        'unread_count': unread_count,
        'site_name': site_name,
        'forum_login_url_name': forum_login_url_name,
        'forum_reg_url_name': forum_reg_url_name
    }
