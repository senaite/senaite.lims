# -*- coding: utf-8 -*-

from plone.app.contentmenu.view import ContentMenuProvider

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SenaiteContentMenuProvider(ContentMenuProvider):
    index = ViewPageTemplateFile('templates/plone.app.contentmenu.contentmenu.pt')
