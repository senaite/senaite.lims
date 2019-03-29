# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE and CONTRIBUTING.

from bika.lims import api
from plone.app.controlpanel.overview import OverviewControlPanel
from plone.memoize.volatile import cache
from plone.memoize.volatile import store_on_context
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter
from zope.interface import implements

from .interfaces import IBootstrapView


def modified_cache_key(method, self, brain_or_object):
    """A cache key that returns the millis of the last modification time
    """
    return api.get_modification_date(brain_or_object).millis()


class SenaiteOverviewControlPanel(OverviewControlPanel):
    template = ViewPageTemplateFile(
        "templates/plone.app.controlpanel.overview.pt")


class BootstrapView(BrowserView):
    """Twitter Bootstrap helper view for SENAITE LIMS
    """
    implements(IBootstrapView)

    def __init__(self, context, request):
        super(BrowserView, self).__init__(context, request)

    @cache(modified_cache_key, store_on_context)
    def get_icon_for(self, brain_or_object):
        """Get the icon for the brain or object
        """
        portal_types = api.get_tool("portal_types")
        fti = portal_types.getTypeInfo(api.get_portal_type(brain_or_object))
        icon = fti.getIcon()
        if not icon:
            return ""
        # Always try to get the big icon for high-res displays
        icon_big = icon.replace(".png", "_big.png")
        # fall back to a default icon if the looked up icon does not exist
        if self.context.restrictedTraverse(icon_big, None) is None:
            icon_big = None
        portal_url = api.get_url(api.get_portal())
        title = api.get_title(brain_or_object)
        html_tag = "<img title='{}' src='{}/{}' width='16' />".format(
            title, portal_url, icon_big or icon)
        return html_tag

    def getViewportValues(self, view=None):
        """Determine the value of the viewport meta-tag
        """
        values = {
            'width': 'device-width',
            'initial-scale': '1.0',
        }

        return ','.join('%s=%s' % (k, v) for k, v in values.items())

    def getColumnsClasses(self, view=None):
        """Determine whether a column should be shown. The left column is
           called plone.leftcolumn; the right column is called
           plone.rightcolumn.
        """

        plone_view = getMultiAdapter(
            (self.context, self.request), name=u'plone')
        portal_state = getMultiAdapter(
            (self.context, self.request), name=u'plone_portal_state')

        sl = plone_view.have_portlets('plone.leftcolumn', view=view)
        sr = plone_view.have_portlets('plone.rightcolumn', view=view)

        isRTL = portal_state.is_rtl()

        # pre-fill dictionary
        columns = dict(one="", content="", two="")

        if not sl and not sr:
            # we don't have columns, thus conten takes the whole width
            columns['content'] = "col-md-12"

        elif sl and sr:
            # In case we have both columns, content takes 50% of the whole
            # width and the rest 50% is spread between the columns
            columns['one'] = "col-xs-12 col-md-2"
            columns['content'] = "col-xs-12 col-md-8"
            columns['two'] = "col-xs-12 col-md-2"

        elif (sr and not sl) and not isRTL:
            # We have right column and we are NOT in RTL language
            columns['content'] = "col-xs-12 col-md-10"
            columns['two'] = "col-xs-12 col-md-2"

        elif (sl and not sr) and isRTL:
            # We have left column and we are in RTL language
            columns['one'] = "col-xs-12 col-md-2"
            columns['content'] = "col-xs-12 col-md-10"

        elif (sl and not sr) and not isRTL:
            # We have left column and we are in NOT RTL language
            columns['one'] = "col-xs-12 col-md-2"
            columns['content'] = "col-xs-12 col-md-10"

        # # append cell to each css-string
        # for key, value in columns.items():
        #     columns[key] = "cell " + value

        return columns
