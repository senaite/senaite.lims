# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE and CONTRIBUTING.

from zope.interface import Interface
from zope.viewlet.interfaces import IViewletManager


class IBelowNavbarSections(IViewletManager):
    """A viewlet manager that sits below the navbar sections
    """


class IBootstrapView(Interface):
    """Twitter Bootstrap View
    """

    def getColumnsClasses(view=None):
        """A helper method to return the clases for the columns of the site
           it should return a dict with three elements:'one', 'two', 'content'
           Each of them should contain the classnames for the first (leftmost)
           second (rightmost) and middle column
        """

    def getViewportValues(view=None):
        """Determine the value of the viewport meta-tag
        """
