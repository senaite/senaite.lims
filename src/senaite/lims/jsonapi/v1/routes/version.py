# -*- coding: utf-8 -*-

from senaite.lims.jsonapi import url_for
from senaite.lims.jsonapi import add_route

from senaite.lims.jsonapi.v1 import __version__
from senaite.lims.jsonapi.v1 import __date__


@add_route("/senaite/v1", "senaite.lims.jsonapi.v1.version", methods=["GET"])
@add_route("/senaite/v1/version", "senaite.lims.jsonapi.v1.version", methods=["GET"])
def version(context, request):
    """get the version, build number and date of this API
    """
    return {
        "url":     url_for("senaite.lims.jsonapi.v1.version"),
        "version": __version__,
        "date":    __date__,
    }
