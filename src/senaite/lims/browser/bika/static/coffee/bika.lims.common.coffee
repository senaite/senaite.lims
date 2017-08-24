### Please use this command to compile this file into the parent `js` directory:
    coffee --no-header -w -o ../js -c bika.lims.common.coffee

    SENAITE Changes:
      - portalMessage markup
###


window.CommonUtils = ->
  that = this

  ###*
  # Entry-point method for CommonUtils
  ###

  that.load = ->
    window.bika = window.bika or lims: {}

    ###*
    # Analysis Service dependants and dependencies retrieval
    ###

    window.bika.lims.AnalysisService = window.bika.lims.AnalysisService or
      Dependants: (service_uid) ->
        request_data = 
          catalog_name: 'bika_setup_catalog'
          UID: service_uid
        deps = {}
        $.ajaxSetup async: false
        window.bika.lims.jsonapi_read request_data, (data) ->
          if data.objects != null and data.objects.length > 0
            deps = data.objects[0].ServiceDependants
          else
            deps = []
          return
        $.ajaxSetup async: true
        deps
      Dependencies: (service_uid) ->
        request_data = 
          catalog_name: 'bika_setup_catalog'
          UID: service_uid
        deps = {}
        $.ajaxSetup async: false
        window.bika.lims.jsonapi_read request_data, (data) ->
          if data.objects != null and data.objects.length > 0
            deps = data.objects[0].ServiceDependencies
          else
            deps = []
          return
        $.ajaxSetup async: true
        deps

    window.bika.lims.portalMessage = (message) ->
      str = '<dl class=\'portalMessage alert alert-danger\'>' + '<dt>' + _('Error') + '</dt>' + '<dd><ul>' + message + '</ul></dd></dl>'
      $('.portalMessage').remove()
      $(str).appendTo '#viewlet-above-content'
      return

    window.bika.lims.log = (e) ->
      if window.location.url == undefined or window.location.url == null
        return
      message = '(' + window.location.url + '): ' + e
      $.ajax
        type: 'POST'
        url: 'js_log'
        data:
          'message': message
          '_authenticator': $('input[name=\'_authenticator\']').val()
      return

    window.bika.lims.error = (e) ->
      message = '(' + window.location.href + '): ' + e
      $.ajax
        type: 'POST'
        url: 'js_err'
        data:
          'message': message
          '_authenticator': $('input[name=\'_authenticator\']').val()
      return

    window.bika.lims.jsonapi_cache = {}

    window.bika.lims.jsonapi_read = (request_data, handler) ->
      window.bika.lims.jsonapi_cache = window.bika.lims.jsonapi_cache or {}
      # if no page_size is specified, we need to explicitly add one here: 0=all.
      page_size = request_data.page_size
      if page_size == undefined
        request_data.page_size = 0
      jsonapi_cacheKey = $.param(request_data)
      jsonapi_read_handler = handler
      if window.bika.lims.jsonapi_cache[jsonapi_cacheKey] == undefined
        $.ajax
          type: 'POST'
          dataType: 'json'
          url: window.portal_url + '/@@API/read'
          data: request_data
          success: (data) ->
            window.bika.lims.jsonapi_cache[jsonapi_cacheKey] = data
            jsonapi_read_handler data
            return
      else
        jsonapi_read_handler window.bika.lims.jsonapi_cache[jsonapi_cacheKey]
      return

    return

  that.svgToImage = (svg) ->
    url = 'data:image/svg+xml;base64,' + btoa(svg)
    '<img src="' + url + '"/>'

  return
