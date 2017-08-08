# -*- coding: utf-8 -*-

from zope.interface import Interface  # noqa
from bika.lims.interfaces import IBikaLIMS


class ISenaiteLIMS(IBikaLIMS):
    """Marker interface that defines a Zope 3 browser layer.
    A layer specific for this add-on product.
    This interface is referred in browserlayer.xml.
    All views and viewlets register against this layer will appear on
    your Plone site only when the add-on installer has been run.
    """
