# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE and CONTRIBUTING.

from plone.app.contentmenu.view import ContentMenuProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from ZPublisher.BaseRequest import DefaultPublishTraverse
from zope.interface import Interface
from zope.component import queryMultiAdapter


class SenaiteContentMenuProvider(ContentMenuProvider):
    index = ViewPageTemplateFile(
        "templates/plone.app.contentmenu.contentmenu.pt")


class SenaiteAppTraverser(DefaultPublishTraverse):
    def publishTraverse(self, request, name):
        if name == "index_html":
            view = queryMultiAdapter(
                (self.context, request),
                Interface, "senaite-overview")
            if view is not None:
                return view
        return DefaultPublishTraverse.publishTraverse(self, request, name)
