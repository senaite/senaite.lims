# -*- coding: utf-8 -*-
#
# Copyright 2017-2017 SENAITE LIMS.

import logging
from zope.i18nmessageid import MessageFactory

# Defining a Message Factory for when this product is internationalized.
senaiteMessageFactory = MessageFactory('senaite.lims')

logger = logging.getLogger("SENAITE")


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    logger.info("*** Initializing SENAITE LIMS Customization Package ***")
