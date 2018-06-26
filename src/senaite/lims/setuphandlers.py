# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE and CONTRIBUTING.

from senaite.lims import logger


def setup_handler(context):
    """Generic setup handler
    """

    if context.readDataFile('senaite.lims.txt') is None:
        return

    logger.info("SENAITE setup handler [BEGIN]")
    portal = context.getSite()  # noqa
    logger.info("SENAITE setup handler [DONE]")


def post_install(portal_setup):
    """Runs after the last import step of the *default* profile

    This handler is registered as a *post_handler* in the generic setup profile

    :param portal_setup: SetupTool
    """
    logger.info("SENAITE LIMS install handler [BEGIN]")

    # https://docs.plone.org/develop/addons/components/genericsetup.html#custom-installer-code-setuphandlers-py
    profile_id = "profile-senaite.lims:default"
    context = portal_setup._getImportContext(profile_id)
    portal = context.getSite()  # noqa

    logger.info("SENAITE LIMS install handler [DONE]")


def post_uninstall(portal_setup):
    """Runs after the last import step of the *uninstall* profile

    This handler is registered as a *post_handler* in the generic setup profile

    :param portal_setup: SetupTool
    """
    logger.info("SENAITE LIMS uninstall handler [BEGIN]")

    # https://docs.plone.org/develop/addons/components/genericsetup.html#custom-installer-code-setuphandlers-py
    profile_id = "profile-senaite.lims:uninstall"
    context = portal_setup._getImportContext(profile_id)
    portal = context.getSite()  # noqa

    logger.info("SENAITE LIMS uninstall handler [DONE]")
