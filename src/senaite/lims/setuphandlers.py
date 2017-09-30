# -*- coding: utf-8 -*-
#
# Copyright 2017-2017 SENAITE LIMS.

from zope import component

from plone.portlets.interfaces import IPortletType

from senaite.lims import logger


def setupHandler(context):
    """SENAITE setup handler
    """

    if context.readDataFile('senaite.lims.txt') is None:
        return

    logger.info("SENAITE setup handler [BEGIN]")

    portal = context.getSite()  # noqa

    # Run Installers
    setup_left_portlet_column(portal)
    setup_right_portlet_column(portal)

    logger.info("SENAITE setup handler [DONE]")


def setup_left_portlet_column(portal):
    """Setup left column portlets
    """
    logger.info("********** Setup left portlet columns")
    mapping = portal.restrictedTraverse('++contextportlets++plone.leftcolumn')

    # delete all portlets on the left
    for key in mapping.keys():
        del mapping[key]

    # create a new navigation portlet
    navigation_portlet = component.getUtility(IPortletType, name='portlets.Navigation')
    addview = mapping.restrictedTraverse('+/' + navigation_portlet.addview)
    data = dict(name=u"Navigation",
                root=None,
                currentFolderOnly=False,
                includeTop=False,
                topLevel=0,
                bottomLevel=0)
    addview.createAndAdd(data)

    # make the navigation portlet the first portlet
    order = list(mapping.keys())
    order.insert(0, order.pop())
    logger.info("********** Changed portlet order from %s to %s" % (repr(list(mapping.keys())), repr(order)))
    mapping.updateOrder(order)


def setup_right_portlet_column(portal):
    """Setup right column portlets
    """
    logger.info("********** Setup right portlet columns")
    mapping = portal.restrictedTraverse('++contextportlets++plone.rightcolumn')

    for key in ['news', 'events', 'Calendar']:
        if key in mapping:
            del mapping[key]
