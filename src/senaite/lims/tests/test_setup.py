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

from Products.CMFPlone.utils import get_installer
from senaite.lims.tests.base import SimpleTestCase


class TestPackagesInstalled(SimpleTestCase):
    """Test if all dependent packages are installed
    """

    def test_is_senaite_core_installed(self):
        qi = get_installer(self.portal)
        self.assertTrue(qi.is_product_installed("senaite.core"))

    def test_is_senaite_lims_installed(self):
        qi = get_installer(self.portal)
        self.assertTrue(qi.is_product_installed("senaite.lims"))

    def test_is_senaite_impress_installed(self):
        qi = get_installer(self.portal)
        self.assertTrue(qi.is_product_installed("senaite.impress"))

    def test_is_senaite_app_listing_installed(self):
        qi = get_installer(self.portal)
        self.assertTrue(qi.is_product_installed("senaite.app.listing"))


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestPackagesInstalled))
    return suite
