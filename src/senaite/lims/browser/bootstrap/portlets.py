# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE and CONTRIBUTING.

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.portlets.portlets.navigation import Renderer as NavigationPortletRenderer


class SenaiteNavigationPortletRenderer(NavigationPortletRenderer):
    _template = ViewPageTemplateFile('templates/plone.app.portlets.portlets.navigation.pt')
    recurse = ViewPageTemplateFile('templates/plone.app.portlets.portlets.navigation_recurse.pt')
