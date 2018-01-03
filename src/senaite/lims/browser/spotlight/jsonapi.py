# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE and CONTRIBUTING.

from senaite import api
from senaite.jsonapi import add_route


@add_route("/spotlight/search", "senaite.lims.spotlight", methods=["GET"])
def spotlight_search_route(context, request):
    """The spotlight search route
    """
    catalogs = [
        "portal_catalog",
        "bika_setup_catalog",
        "bika_catalog",
        # "bika_analysis_catalog"
    ]

    search_results = []
    for catalog in catalogs:
        search_results.extend(search(catalog=catalog))

    def get_state(brain):
        state = getattr(brain, "review_state", "")
        if not isinstance(state, basestring):
            return ""
        return state

    items = []
    for brain in search_results:
        icon = api.get_icon(brain)
        # avoid 404 errors with these guys
        if "document_icon.gif" in icon:
            icon = ""

        id = api.get_id(brain)
        title = api.get_title(brain)

        items.append({
            "id": id,
            "title": title,
            "title_or_id": title or id,
            "description": api.get_description(brain),
            "uid": api.get_uid(brain),
            "path": api.get_path(brain),
            "url": api.get_url(brain),
            "state": get_state(brain),
            "icon": icon,
        })

    return {
        "count": len(items),
        "items": items,
    }


def search(query=None, catalog=None):
    """Search
    """
    if query is None:
        query = make_query()
    if query is None:
        return []
    return api.search(query, catalog=catalog)


def make_query():
    """A function to prepare a query
    """
    query = {}
    request = api.get_request()

    limit = request.form.get("limit")

    q = request.form.get("q")
    if q:
        query["SearchableText"] = q + "*"
    else:
        return None

    portal_type = request.form.get("portal_type")
    if portal_type:
        if not isinstance(portal_type, list):
            portal_type = [portal_type]
        query["portal_type"] = portal_type

    if limit and limit.isdigit():
        query["sort_limit"] = int(limit)

    return query
