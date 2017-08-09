# -*- coding: utf-8 -*-

from zope.interface import Interface


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
