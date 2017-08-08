# -*- coding: utf-8 -*-

from senaite.lims.tests.base import SimpleTestCase


class TestSetup(SimpleTestCase):
    """ Test Setup
    """

    def test_is_bika_lims_installed(self):
        qi = self.portal.portal_quickinstaller
        self.assertTrue(qi.isProductInstalled("bika.lims"))

    def test_is_senaite_lims_installed(self):
        qi = self.portal.portal_quickinstaller
        self.assertTrue(qi.isProductInstalled("senaite.lims"))


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestSetup))
    return suite
