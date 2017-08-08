# -*- coding: utf-8 -*-

from senaite.lims.jsonapi import api
from senaite.lims.jsonapi.v1 import add_route
from senaite.lims.jsonapi.exceptions import APIError

ACTIONS = "create,update,delete"


# /<resource (portal_type)>
@add_route("/<string:resource>",
           "senaite.lims.jsonapi.v1.get", methods=["GET"])
#
# /<resource (portal_type)>/<uid>
@add_route("/<string:resource>/<string(maxlength=32):uid>",
           "senaite.lims.jsonapi.v1.get", methods=["GET"])
def get(context, request, resource=None, uid=None):
    """GET
    """
    # we have a UID as resource, return the record
    if api.is_uid(resource):
        return api.get_record(resource)

    portal_type = api.resource_to_portal_type(resource)
    if portal_type is None:
        raise APIError(404, "Not Found")
    return api.get_batched(portal_type=portal_type, uid=uid, endpoint="senaite.lims.jsonapi.v1.get")


# http://werkzeug.pocoo.org/docs/0.11/routing/#builtin-converters
# http://werkzeug.pocoo.org/docs/0.11/routing/#custom-converters
#
# /<uid>
@add_route("/<any(" + ACTIONS + "):action>",
           "senaite.lims.jsonapi.v1.action", methods=["POST"])
#
# /<action (create,update,delete)>/<uid>
@add_route("/<any(" + ACTIONS + "):action>/<string(maxlength=32):uid>",
           "senaite.lims.jsonapi.v1.action", methods=["POST"])
#
# /<resource (portal_type)>/<action (create,update,delete)>
@add_route("/<string:resource>/<any(" + ACTIONS + "):action>",
           "senaite.lims.jsonapi.v1.action", methods=["POST"])
#
# /<resource (portal_type)>/<action (create,update,delete)>/<uid>
@add_route("/<string:resource>/<any(" + ACTIONS + "):action>/<string(maxlength=32):uid>",
           "senaite.lims.jsonapi.v1.action", methods=["POST"])
def action(context, request, action=None, resource=None, uid=None):
    """Various HTTP POST actions

    Case 1: /<uid>
    -> Return the full object immediately in the root of the JSON API response
    <Senaite-Site>/@@API/senaite/v1/<uid>

    Case 2: /<action>/<uid>
    -> The actions (update, delete) will performed on the object identified by <uid>
    -> The actions (create) will use the <uid> as the parent folder
    <Senaite-Site>/@@API/senaite/v1/<action>/<uid>

    Case 3: <resource>/<action>
    -> The "target" object will be located by a location given in the request body (uid, path, parent_path + id)
    -> The actions (cut, copy, update, delete) will performed on the target object
    -> The actions (create) will use the target object as the container
    <Senaite-Site>/@@API/senaite/v1/<resource>/<action>

    Case 4: <resource>/<action>/<uid>
    -> The actions (cut, copy, update, delete) will performed on the object identified by <uid>
    -> The actions (create) will use the <uid> as the parent folder
    <Senaite-Site>/@@API/senaite/v1/<resource>/<action>
    """

    # Fetch and call the action function of the API
    func_name = "{}_items".format(action)
    action_func = getattr(api, func_name, None)
    if action_func is None:
        api.fail(500, "API has no member named '{}'".format(func_name))

    portal_type = api.resource_to_portal_type(resource)
    items = action_func(portal_type=portal_type, uid=uid)

    return {
        "count": len(items),
        "items": items,
        "url": api.url_for("senaite.lims.jsonapi.v1.action", action=action),
    }


@add_route("/search",
           "senaite.lims.jsonapi.v1.search", methods=["GET"])
def search(context, request):
    """Generic search route

    <Plonesite>/@@API/v2/search -> returns all contents of the portal
    <Plonesite>/@@API/v2/search?portal_type=Folder -> returns only folders
    ...
    """
    return api.get_batched()
