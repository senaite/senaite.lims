# -*- coding: utf-8 -*-

from senaite.lims import logger


def setupHandler(context):
    """SENAITE setup handler
    """

    if context.readDataFile('senaite.lims.txt') is None:
        return

    logger.info("SENAITE setup handler [BEGIN]")

    portal = context.getSite()  # noqa

    # Run Installers

    logger.info("SENAITE setup handler [DONE]")
