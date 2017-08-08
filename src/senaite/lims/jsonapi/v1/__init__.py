# -*- coding: utf-8 -*-

import pkgutil

from senaite.lims import logger
from senaite.lims.jsonapi.v1 import routes
from senaite.lims.jsonapi import add_route as add_senaite_route

__version__ = 1
__date__ = "2017-08-08"

BASE_URL = "/senaite/v1"


def add_route(route, endpoint=None, **kw):
    """Add a new JSON API route
    """

    # ensure correct amout of slashes
    def apiurl(route):
        return '/'.join(s.strip('/') for s in ["", BASE_URL, route])

    return add_senaite_route(apiurl(route), endpoint, **kw)


prefix = routes.__name__ + "."
for importer, modname, ispkg in pkgutil.iter_modules(
        routes.__path__, prefix):
    module = __import__(modname, fromlist="dummy")
    logger.info("INITIALIZED SENAITE JSONAPI V1 ROUTE ---> %s" % module.__name__)
