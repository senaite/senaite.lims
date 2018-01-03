# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE and CONTRIBUTING.

from plone.app.contentmenu.view import ContentMenuProvider

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SenaiteContentMenuProvider(ContentMenuProvider):
    index = ViewPageTemplateFile('templates/plone.app.contentmenu.contentmenu.pt')
