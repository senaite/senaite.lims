# -*- coding: utf-8 -*-

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets.common import LogoViewlet
from plone.app.layout.viewlets.common import ContentViewsViewlet
from plone.app.layout.viewlets.common import PathBarViewlet
from plone.app.layout.viewlets.common import PersonalBarViewlet


class SenaiteLogoViewlet(LogoViewlet):
    index = ViewPageTemplateFile('templates/plone.app.layout.viewlets.logo.pt')


class SenaiteContentViewsViewlet(ContentViewsViewlet):
    index = ViewPageTemplateFile('templates/plone.app.layout.viewlets.contentviews.pt')


class SenaitePathBarViewlet(PathBarViewlet):
    index = ViewPageTemplateFile('templates/plone.app.layout.viewlets.path_bar.pt')


class SenaitePersonalBarViewlet(PersonalBarViewlet):
    index = ViewPageTemplateFile('templates/plone.app.layout.viewlets.personal_bar.pt')
