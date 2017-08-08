# -*- coding: utf-8 -*-
#
# Copyright 2016-2017 BECHEM GmbH.

import doctest

import unittest2 as unittest

from Testing import ZopeTestCase as ztc

from .base import SimpleTestCase


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        ztc.ZopeDocFileSuite(
            '../docs/API.rst',
            test_class=SimpleTestCase,
            optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE,
        ),
    ])
    return suite
