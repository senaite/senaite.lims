# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE and CONTRIBUTING.

from cgi import escape

from Acquisition import aq_inner
from bika.lims.browser.instrument import InstrumentQCFailuresViewlet
from bika.lims.browser.viewlets.attachments import AttachmentsViewlet
from bika.lims.browser.viewlets.attachments import WorksheetAttachmentsViewlet
from plone.app.customerize import registration
from plone.app.layout.viewlets.common import ContentViewsViewlet
from plone.app.layout.viewlets.common import FooterViewlet
from plone.app.layout.viewlets.common import GlobalSectionsViewlet
from plone.app.layout.viewlets.common import LogoViewlet
from plone.app.layout.viewlets.common import PathBarViewlet
from plone.app.layout.viewlets.common import PersonalBarViewlet
from plone.app.layout.viewlets.common import SiteActionsViewlet
from plone.app.layout.viewlets.common import ViewletBase
from plone.app.layout.viewlets.content import DocumentActionsViewlet
from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zExceptions import NotFound
from zope.component import getMultiAdapter
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.viewlet.interfaces import IViewlet


class SenaiteLogoViewlet(LogoViewlet):
    index = ViewPageTemplateFile(
        'templates/plone.app.layout.viewlets.logo.pt')

    def update(self):
        super(LogoViewlet, self).update()

        portal = self.portal_state.portal()
        bprops = portal.restrictedTraverse("base_properties", None)
        if bprops is not None:
            logoName = bprops.logoName
        else:
            logoName = "logo.jpg"

        logoTitle = self.portal_state.portal_title()
        self.logo_tag = portal.restrictedTraverse(logoName).tag(
            title=logoTitle, alt=logoTitle, scale=0.5)
        self.navigation_root_title = self.portal_state.navigation_root_title()


class SenaiteGlobalSectionsViewlet(GlobalSectionsViewlet):
    index = ViewPageTemplateFile(
        'templates/plone.app.layout.viewlets.sections.pt')

    def update(self):
        super(SenaiteGlobalSectionsViewlet, self).update()
        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        self.navigation_root_url = portal_state.navigation_root_url()
        self.portal_title = escape(
            safe_unicode(portal_state.navigation_root_title()))


class SenaiteSectionsDropdownViewlet(GlobalSectionsViewlet):
    index = ViewPageTemplateFile(
        'templates/senaite.lims.browser.bootstrap.viewlets.sections_dropdown.pt')

    def update(self):
        super(SenaiteSectionsDropdownViewlet, self).update()
        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        self.navigation_root_url = portal_state.navigation_root_url()
        self.portal_title = escape(
            safe_unicode(portal_state.navigation_root_title()))


class SenaitePathBarViewlet(PathBarViewlet):
    index = ViewPageTemplateFile(
        'templates/plone.app.layout.viewlets.path_bar.pt')


class SenaitePersonalBarViewlet(PersonalBarViewlet):
    index = ViewPageTemplateFile(
        'templates/plone.app.layout.viewlets.personal_bar.pt')


class SenaitePersonalNavBarViewlet(PersonalBarViewlet):
    index = ViewPageTemplateFile(
        'templates/senaite.lims.browser.bootstrap.viewlets.personal_nav_bar.pt')


class SenaiteContentViewsViewlet(ContentViewsViewlet):
    index = ViewPageTemplateFile(
        'templates/plone.app.layout.viewlets.contentviews.pt')


class SenaiteSiteActionsViewlet(SiteActionsViewlet):
    index = ViewPageTemplateFile(
        "templates/plone.app.layout.viewlets.site_actions.pt")


class SenaiteDocumentActionsViewlet(DocumentActionsViewlet):
    index = ViewPageTemplateFile(
        'templates/plone.app.layout.viewlets.documentactions.pt')


class SenaiteColophonViewlet(ViewletBase):
    index = ViewPageTemplateFile(
        'templates/plone.app.layout.viewlets.colophon.pt')


class SenaiteFooterViewlet(FooterViewlet):
    index = ViewPageTemplateFile(
        'templates/plone.app.layout.viewlets.footer.pt')


class SenaiteInstrumentQCFailuresViewlet(InstrumentQCFailuresViewlet):
    index = ViewPageTemplateFile(
        'templates/bika.lims.browser.templates.instrument_qc_failures_viewlet.pt')


class SenaiteAttachmentsViewlet(AttachmentsViewlet):
    template = ViewPageTemplateFile(
        'templates/bika.lims.browser.viewlets.templates.attachments.pt')


class SenaiteWorksheetAttachmentsViewlet(WorksheetAttachmentsViewlet):
    template = ViewPageTemplateFile(
        'templates/bika.lims.browser.viewlets.templates.worksheet_attachments.pt')


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
