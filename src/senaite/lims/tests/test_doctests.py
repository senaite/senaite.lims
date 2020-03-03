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
# Copyright 2018-2020 by it's authors.
# Some rights reserved, see README and LICENSE.

import unittest2 as unittest

# from Testing import ZopeTestCase as ztc

# from .base import SimpleTestCase


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        # ztc.ZopeDocFileSuite(
        #     '../docs/API.rst',
        #     test_class=SimpleTestCase,
        #     optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE,
        # ),
    ])
    return suite
