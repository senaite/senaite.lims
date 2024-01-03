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
# Copyright 2018-2024 by it's authors.
# Some rights reserved, see README and LICENSE.

import transaction
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import TEST_USER_PASSWORD
from plone.app.testing import FunctionalTesting
from plone.app.testing.bbb_at import PloneTestCase
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import setRoles
from plone.protect.authenticator import createToken
from plone.testing import zope
from plone.testing.zope import Browser


class SimpleTestLayer(PloneSandboxLayer):
    """Setup Plone with installed AddOn only
    """
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        super(SimpleTestLayer, self).setUpZope(app, configurationContext)

        # Load ZCML
        import bika.lims
        import senaite.core
        import senaite.lims
        import senaite.impress
        import senaite.app.listing
        import senaite.app.spotlight

        self.loadZCML(package=bika.lims)
        self.loadZCML(package=senaite.core)
        self.loadZCML(package=senaite.lims)
        self.loadZCML(package=senaite.impress)
        self.loadZCML(package=senaite.app.listing)
        self.loadZCML(package=senaite.app.spotlight)

        # Install product and call its initialize() function
        zope.installProduct(app, "bika.lims")
        zope.installProduct(app, "senaite.core")
        zope.installProduct(app, "senaite.app.listing")
        zope.installProduct(app, "senaite.app.spotlight")
        zope.installProduct(app, "senaite.impress")
        zope.installProduct(app, "senaite.lims")

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        applyProfile(portal, "senaite.lims:default")
        transaction.commit()


###
# Use for simple tests (w/o contents)
###
SIMPLE_FIXTURE = SimpleTestLayer()
SIMPLE_TESTING = FunctionalTesting(
    bases=(SIMPLE_FIXTURE, ),
    name="senaite.lims:SimpleTesting"
)


class SimpleTestCase(PloneTestCase):
    layer = SIMPLE_TESTING

    def setUp(self):
        super(SimpleTestCase, self).setUp()
        # Fixing CSRF protection
        # https://github.com/plone/plone.protect/#fixing-csrf-protection-failures-in-tests
        self.request = self.layer["request"]
        # Disable plone.protect for these tests
        self.request.form["_authenticator"] = createToken()
        # Eventuelly you find this also useful
        self.request.environ["REQUEST_METHOD"] = "POST"

        setRoles(self.portal, TEST_USER_ID, ["LabManager", "Manager"])

        # Default skin is set to "Sunburst Theme"!
        # => This causes an `AttributeError` when we want to access
        #    e.g. 'guard_handler' FSPythonScript
        self.portal.changeSkin("Plone Default")

    def getBrowser(self,
                   username=TEST_USER_NAME,
                   password=TEST_USER_PASSWORD,
                   loggedIn=True):

        # Instantiate and return a testbrowser for convenience
        browser = Browser(self.portal)
        browser.addHeader("Accept-Language", "en-US")
        browser.handleErrors = False
        if loggedIn:
            browser.open(self.portal.absolute_url())
            browser.getControl("Login Name").value = username
            browser.getControl("Password").value = password
            browser.getControl("Log in").click()
            self.assertTrue("You are now logged in" in browser.contents)
        return browser
