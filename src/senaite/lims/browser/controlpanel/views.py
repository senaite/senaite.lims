# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE and CONTRIBUTING.

import os
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
# from zope.interface import implements
from senaite import api


class LIMSControlPanel(BrowserView):
    """SENAITE LIMS Control Panel
    """
    template = ViewPageTemplateFile("templates/overview.pt")

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        self.request.set("disable_border", 1)
        return self.template()

    @property
    def portal(self):
        return api.get_portal()

    @property
    def setup(self):
        return api.get_setup()

    def get_icon_url(self, brain):
        """
        """
        icon_url = api.get_icon(brain, html_tag=False)
        url, icon = icon_url.rsplit("/", 1)
        relative_url = url.lstrip(self.portal.absolute_url())
        name, ext = os.path.splitext(icon)

        if not name.endswith("_big"):
            icon = "{}_big{}".format(name, ext)

        icon_big_url = "/".join([relative_url, icon])

        if self.context.restrictedTraverse(icon_big_url, None) is None:
            icon_big_url = "++resource++senaite.lims.images/gears.png"

        return icon_big_url

    def controlpanels(self):
        """LIMS Control Panels (tiles)
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
