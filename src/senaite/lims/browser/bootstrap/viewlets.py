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

from Acquisition import aq_inner
from plone.app.customerize import registration
from plone.app.layout.viewlets.common import ContentViewsViewlet
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zExceptions import NotFound
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.viewlet.interfaces import IViewlet


class SenaiteContentViewsViewlet(ContentViewsViewlet):
    index = ViewPageTemplateFile(
        'templates/plone.app.layout.viewlets.contentviews.pt')


class ViewletView(BrowserView):
    """Expose arbitrary viewlets to traversing by name.

    Example how to render plone.logo viewlet in arbitrary template code point::

        <div tal:content="context/@@viewlets/plone.logo" />

    https://docs.plone.org/develop/plone/views/viewlets.html#rendering-viewlet-by-name
    """

    def __init__(self, context, request):
        super(ViewletView, self).__init__(context, request)
        self.context = context
        self.request = request

    def getViewletByName(self, name):

        """ Viewlets allow through-the-web customizations.

        Through-the-web customization magic is managed by five.customerize.
        We need to think of this when looking up viewlets.

        @return: Viewlet registration object
        """
        views = registration.getViews(IBrowserRequest)

        for v in views:

            if v.provided == IViewlet:
                # Note that we might have conflicting BrowserView with the same
                # name, thus we need to check for provided
                if v.name == name:
                    return v

        return None

    def setupViewletByName(self, name):
        """ Constructs a viewlet instance by its name.

        Viewlet update() and render() method are not called.

        @return: Viewlet instance of None if viewlet with name does not exist
        """
        context = aq_inner(self.context)
        request = self.request

        # Perform viewlet regisration look-up
        # from adapters registry
        reg = self.getViewletByName(name)
        if reg is None:
            return None

        # factory method is responsible for creating the viewlet instance
        factory = reg.factory

        # Create viewlet and put it to the acquisition chain
        # Viewlet need initialization parameters: context, request, view
        try:
            viewlet = factory(context, request, self, None).__of__(context)
        except TypeError:
            # Bad constructor call parameters
            raise RuntimeError(
                "Unable to initialize viewlet {}. "
                "Factory method {} call failed."
                .format(name, str(factory)))

        return viewlet

    def __getitem__(self, name):
        """Allow travering intoviewlets by viewlet name.
        """
        viewlet = self.setupViewletByName(name)
        if viewlet is None:
            raise NotFound("Viewlet {} not found".format(name))
        viewlet.update()
        return viewlet.render()
