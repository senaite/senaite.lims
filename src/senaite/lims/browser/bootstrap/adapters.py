# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS.
#
# SENAITE.LIMS is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright 2018-2019 by it's authors.
# Some rights reserved, see README and LICENSE.

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
