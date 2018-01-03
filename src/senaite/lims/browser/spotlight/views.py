# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE and CONTRIBUTING.

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from senaite.lims import senaiteMessageFactory as _


class SpotlightView(BrowserView):
    """The spotlight search view just renders the template
    """
    template = ViewPageTemplateFile("templates/spotlight.pt")
    viewlet = ViewPageTemplateFile("templates/spotlight_viewlet.pt")

    def __init__(self, context, request):
        request.set('disable_border', 1)
        self.context = context
        self.request = request
        self.css_class = "spotlight-view"
        self.placeholder = _("Search ...")
        self.viewlet = self.viewlet()

    def __call__(self):
        return self.template()
