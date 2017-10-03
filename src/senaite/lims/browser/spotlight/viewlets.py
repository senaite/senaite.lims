# -*- coding: utf-8 -*-
#
# Copyright 2017-2017 SENAITE LIMS.

from plone.app.layout.viewlets.common import ViewletBase

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from senaite.lims import senaiteMessageFactory as _


class SpotlightViewlet(ViewletBase):
    """The spotlight search viewlet renders on all pages
    """
    index = ViewPageTemplateFile("templates/spotlight_viewlet.pt")

    def __init__(self, context, request, view, manager):
        super(SpotlightViewlet, self).__init__(context, request, view, manager)
        self.css_class = "spotlight-overlay"
        self.placeholder = _("Spotlight Search ...")

    def update(self):
        pass
