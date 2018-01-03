# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE and CONTRIBUTING.

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
