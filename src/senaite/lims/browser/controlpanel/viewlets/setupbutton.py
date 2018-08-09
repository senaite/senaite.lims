# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE and CONTRIBUTING.

from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from senaite import api


class SenaiteSetupButtonViewlet(ViewletBase):
    """Renders a Button to navigate to the Setup View
    """
    index = ViewPageTemplateFile("templates/setupbutton.pt")

    def update(self):
        super(SenaiteSetupButtonViewlet, self).update()
        self.portal = api.get_portal()
        portal_url = self.portal.absolute_url()
        self.setup_url = "/".join([portal_url, "@@lims-setup"])
