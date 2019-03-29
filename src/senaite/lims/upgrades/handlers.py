# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS
#
# Copyright 2018-2019 by it's authors.

from senaite.impress import logger
from senaite.lims.setuphandlers import setup_html_filter

PROFILE_ID = "profile-senaite.lims:default"


def to_1000(portal_setup):
    """Initial version to 1000

    :param portal_setup: The portal_setup tool
    """

    logger.info("Run all import steps from SENAITE LIMS ...")
    context = portal_setup._getImportContext(PROFILE_ID)
    portal = context.getSite()
    setup_html_filter(portal)
    portal_setup.runAllImportStepsFromProfile(PROFILE_ID)
    logger.info("Run all import steps from SENAITE LIMS [DONE]")
