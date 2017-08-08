# -*- coding: utf-8 -*-

import unittest2 as unittest

from plone.testing import z2

from plone.app.testing import setRoles
from plone.app.testing import applyProfile
from plone.app.testing import TEST_USER_ID
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import FunctionalTesting

from bika.lims.testing import BIKA_SIMPLE_FIXTURE
from bika.lims.testing import BIKA_FUNCTIONAL_FIXTURE


class SimpleTestLayer(PloneSandboxLayer):
    """Setup Plone with installed AddOn only
    """
    defaultBases = (BIKA_SIMPLE_FIXTURE, PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        super(SimpleTestLayer, self).setUpZope(app, configurationContext)

        # Load ZCML
        import senaite.lims

        self.loadZCML(package=senaite.lims)

        # Install product and call its initialize() function
        z2.installProduct(app, 'senaite.lims')

    def setUpPloneSite(self, portal):
        super(SimpleTestLayer, self).setUpPloneSite(portal)

        # Apply Setup Profile (portal_quickinstaller)
        applyProfile(portal, 'senaite.lims:default')


class FunctionalTestLayer(SimpleTestLayer):
    """Setup Plone for functional Tests
    """
    defaultBases = (BIKA_FUNCTIONAL_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        super(FunctionalTestLayer, self).setUpZope(app, configurationContext)

    def setUpPloneSite(self, portal):
        super(FunctionalTestLayer, self).setUpPloneSite(portal)


###
# Use for simple tests (w/o contents)
###
SIMPLE_FIXTURE = SimpleTestLayer()
SIMPLE_TESTING = FunctionalTesting(
    bases=(SIMPLE_FIXTURE, ),
    name="senaite.lims:SimpleTesting"
)

###
# Use for functional tests (w/ contents)
# Using this Layer takes approx. 1 minute to load
###
FUNCTIONAL_FIXTURE = FunctionalTestLayer()
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FUNCTIONAL_FIXTURE, ),
    name="senaite.lims:FunctionalTesting"
)


class SimpleTestCase(unittest.TestCase):
    layer = SIMPLE_TESTING

    def setUp(self):
        super(SimpleTestCase, self).setUp()

        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.request['ACTUAL_URL'] = self.portal.absolute_url()
        setRoles(self.portal, TEST_USER_ID, ['LabManager', 'Manager'])


class FunctionalTestCase(unittest.TestCase):
    layer = FUNCTIONAL_TESTING

    def setUp(self):
        super(FunctionalTestCase, self).setUp()

        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.request['ACTUAL_URL'] = self.portal.absolute_url()
        setRoles(self.portal, TEST_USER_ID, ['LabManager', 'Member'])
