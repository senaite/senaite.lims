# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS.
#
# SENAITE.LIMS is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright 2018-2019 by it's authors.
# Some rights reserved, see README and LICENSE.

from operator import itemgetter

from bika.lims.catalog.analysisrequest_catalog import \
    CATALOG_ANALYSIS_REQUEST_LISTING
from plone.memoize import forever
from senaite import api
from senaite.jsonapi import add_route


@add_route("/spotlight/search", "senaite.lims.spotlight", methods=["GET"])
def spotlight_search_route(context, request):
    """The spotlight search route
    """
    catalogs = [
        CATALOG_ANALYSIS_REQUEST_LISTING,
        "portal_catalog",
        "bika_setup_catalog",
        "bika_catalog",
        "bika_catalog_worksheet_listing"
    ]

    search_results = []
    for catalog in catalogs:
        search_results.extend(search(catalog=catalog))

    # extract the data from all the brains
    items = map(get_brain_info, search_results)

    return {
        "count": len(items),
        "items": sorted(items, key=itemgetter("title")),
    }


def get_brain_info(brain):
    """Extract the brain info
    """
    icon = api.get_icon(brain)
    # avoid 404 errors with these guys
    if "document_icon.gif" in icon:
        icon = ""

    id = api.get_id(brain)
    url = api.get_url(brain)
    title = api.get_title(brain)
    description = api.get_description(brain)
    parent = api.get_parent(brain)
    parent_title = api.get_title(parent)
    parent_url = api.get_url(parent)

    return {
        "id": id,
        "title": title,
        "title_or_id": title or id,
        "description": description,
        "url": url,
        "parent_title": parent_title,
        "parent_url": parent_url,
        "icon": icon,
    }


def search(query=None, catalog=None):
    """Search
    """
    if query is None:
        query = make_query(catalog)
    if query is None:
        return []
    return api.search(query, catalog=catalog)


@forever.memoize
def get_search_index_for(catalog):
    """Returns the search index to query
    """
    searchable_text_index = "SearchableText"
    listing_searchable_text_index = "listing_searchable_text"

    if catalog == CATALOG_ANALYSIS_REQUEST_LISTING:
        tool = api.get_tool(catalog)
        indexes = tool.indexes()
        if listing_searchable_text_index in indexes:
            return listing_searchable_text_index

    return searchable_text_index


def make_query(catalog):
    """A function to prepare a query
    """
    query = {}
    request = api.get_request()
    index = get_search_index_for(catalog)
    limit = request.form.get("limit")

    q = request.form.get("q")
    if len(q) > 0:
        query[index] = q + "*"
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
