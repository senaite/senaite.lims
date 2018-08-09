# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE and CONTRIBUTING.

import os

from plone.memoize.volatile import cache
from plone.memoize.volatile import store_on_context
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from senaite import api


def modified_cache_key(method, self, brain_or_object):
    """A cache key that returns the millis of the last modification time
    """
    return api.get_modification_date(brain_or_object).millis()


class SetupView(BrowserView):
    """SENAITE LIMS Setup View
    """
    template = ViewPageTemplateFile("templates/setupview.pt")

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        self.request.set("disable_border", 1)
        return self.template()

    @property
    def portal(self):
        """Returns the Portal Object
        """
        return api.get_portal()

    @property
    def setup(self):
        """Returns the Senaite Setup Object
        """
        return api.get_setup()

    @cache(modified_cache_key, store_on_context)
    def get_icon_url(self, brain):
        """Returns the (big) icon URL for the given catalog brain
        """
        icon_url = api.get_icon(brain, html_tag=False)
        url, icon = icon_url.rsplit("/", 1)
        relative_url = url.lstrip(self.portal.absolute_url())
        name, ext = os.path.splitext(icon)

        # big icons endwith _big
        if not name.endswith("_big"):
            icon = "{}_big{}".format(name, ext)

        icon_big_url = "/".join([relative_url, icon])

        # fall back to a default icon if the looked up icon does not exist
        if self.context.restrictedTraverse(icon_big_url, None) is None:
            icon_big_url = "++resource++senaite.lims.images/gears.png"

        return icon_big_url

    def setupitems(self):
        """Lookup available setup items

        :returns: catalog brains
        """
        query = {
            "path": {
                "query": api.get_path(self.setup),
                "depth": 1,
            },
            "sort_on": "sortable_title",
            "sort_order": "ascending"
        }
        return api.search(query, "portal_catalog")
