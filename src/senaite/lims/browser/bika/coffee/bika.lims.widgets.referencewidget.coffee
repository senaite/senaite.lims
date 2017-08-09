### Please use this command to compile this file into the parent `js` directory:
    coffee --no-header -w -o ../js -c bika.lims.widgets.referencewidget.coffee
###

debugger

destroy = (arr, val) ->
  i = 0
  while i < arr.length
    if arr[i] == val
      arr.splice i, 1
    i++
  arr

referencewidget_lookups = (elements) ->
  # Any reference widgets that don't already have combogrid widgets
  inputs = undefined
  if elements == undefined
    inputs = $('.ArchetypesReferenceWidget [combogrid_options]').not('.has_combogrid_widget')
  else
    inputs = elements
  i = inputs.length - 1
  while i >= 0
    element = inputs[i]
    options = $.parseJSON($(element).attr('combogrid_options'))
    if !options
      i--
      continue
    # Prevent from saving previous record when input value is empty
    # By default, a recordwidget input element gets an empty value
    # when receives the focus, so the underneath values must be
    # cleared too.
    # var elName = $(element).attr("name");
    # $("input[name='"+elName+"']").live("focusin", function(){
    #  var fieldName = $(this).attr("name");
    #  if($(this).val() || $(this).val().length===0){
    #      var val = $(this).val();
    #      var uid = $(this).attr("uid");
    #      $(this).val("");
    #      $(this).attr("uid", "");
    #      $("input[name='"+fieldName+"_uid']").val("");
    #      $(this).trigger("unselected", [val,uid]);
    #  }
    # });

    options.select = (event, ui) ->
      event.preventDefault()
      fieldName = $(this).attr('name')
      skip = undefined
      uid_element = $(this).siblings('input[$=\'_uid\']')
      listing_div = $(this).siblings('div[id$=\'-listing\']')
      if $(listing_div).length > 0
        # Add selection to textfield value
        existing_value = $(uid_element).val()
        existing_uids = ''
        if existing_value != undefined
          existing_uids = existing_value.split(',')
        destroy existing_uids, ''
        destroy existing_uids, '[]'
        selected_value = ui.item[$(this).attr('ui_item')]
        selected_uid = ui.item.UID
        if existing_uids.indexOf(selected_uid) == -1
          existing_uids.push selected_uid
          $(this).val ''
          $(this).attr 'uid', existing_uids.join(',')
          $(uid_element).val existing_uids.join(',')
          # insert item to listing
          del_btn_src = window.portal_url + '/++resource++bika.lims.images/delete.png'
          del_btn = '<img class=\'deletebtn\' data-contact-title=\'' + ui.item.Title + '\' src=\'' + del_btn_src + '\' fieldName=\'' + fieldName + '\' uid=\'' + selected_uid + '\'/>'
          new_item = '<div class=\'reference_multi_item\' uid=\'' + selected_uid + '\'>' + del_btn + selected_value + '</div>'
          $(listing_div).append $(new_item)
        # skip_referencewidget_lookup: a little cheat
        # it prevents this widget from falling over itself,
        # by allowing other JS to request that the "selected" action
        # is not triggered.
        skip = $(element).attr('skip_referencewidget_lookup')
        if skip != true
          # Pass the entire selected item through to the selected handler
          $(this).trigger 'selected', ui.item
        $(element).removeAttr 'skip_referencewidget_lookup'
        $(this).next('input').focus()
      else
        # Set value in activated element (must exist in colModel!)
        $(this).val ui.item[$(this).attr('ui_item')]
        $(this).attr 'uid', ui.item.UID
        $(uid_element).val ui.item.UID
        skip = $(element).attr('skip_referencewidget_lookup')
        if skip != true
          # Pass the entire selected item through to the selected handler
          $(this).trigger 'selected', ui.item
        $(element).removeAttr 'skip_referencewidget_lookup'
        $(this).next('input').focus()
      return

    if window.location.href.search('portal_factory') > -1
      options.url = window.location.href.split('/portal_factory')[0] + '/' + options.url
    options.url = options.url + '?_authenticator=' + $('input[name=\'_authenticator\']').val()
    options.url = options.url + '&catalog_name=' + $(element).attr('catalog_name')
    options.url = options.url + '&base_query=' + $(element).attr('base_query')
    options.url = options.url + '&search_query=' + $(element).attr('search_query')
    options.url = options.url + '&colModel=' + $.toJSON($.parseJSON($(element).attr('combogrid_options')).colModel)
    options.url = options.url + '&search_fields=' + $.toJSON($.parseJSON($(element).attr('combogrid_options')).search_fields)
    options.url = options.url + '&discard_empty=' + $.toJSON($.parseJSON($(element).attr('combogrid_options')).discard_empty)
    options.url = options.url + '&force_all=' + $.toJSON($.parseJSON($(element).attr('combogrid_options')).force_all)
    $(element).combogrid options
    $(element).addClass 'has_combogrid_widget'
    $(element).attr 'search_query', '{}'
    i--
  return

save_UID_check = ->
  #Save the selected uid's item to avoid introduce non-listed
  #values inside the widget.
  $('.ArchetypesReferenceWidget').bind 'selected', ->
    # None of this stuff should take effect for multivalued widgets;
    # Right now, these must take care of themselves.
    multiValued = $(this).attr('multiValued') == '1'
    if multiValued
      return
    uid = $(this).children('input.referencewidget').attr('uid')
    val = $(this).children('input.referencewidget').val()
    $(this).children('input.referencewidget').attr 'uid_check', uid
    $(this).children('input.referencewidget').attr 'val_check', val
    return
  return

check_UID_check = ->
  #Remove the necessary values to submit if the introduced data is
  #not correct.
  $('.ArchetypesReferenceWidget').children('input.referencewidget').bind 'blur', ->
    # None of this stuff should take effect for multivalued widgets;
    # Right now, these must take care of themselves.
    multiValued = $(this).attr('multiValued') == '1'
    if multiValued
      return
    chk = $(this).attr('uid_check')
    val_chk = $(this).attr('val_check')
    value = $(this).val()
    #When is the first time you click on
    if (chk == undefined or chk == false) and value != '' and $(this).attr('uid')
      $(this).attr 'uid_check', $(this).attr('uid')
      $(this).attr 'val_check', value
    else if (chk == undefined or chk == false) and value != ''
      $(this).attr 'uid', ''
      $(this).attr 'value', ''
    else if $(this).attr('value') and (chk != undefined or chk != false) and chk != $(this).attr('uid')
      $(this).attr 'uid', chk
      $(this).attr 'value', val_chk
    else if val_chk != value and value != ''
      $(this).attr 'uid', chk
      $(this).attr 'value', val_chk
    return
  return

apply_button_overlay = (button) ->

  ###*
  # Given an element (button), this function sets its overlay options.
  # The overlay options to be applied are retrieved from the button's
  # data_overlay attribute.
  # Further info about jQuery overlay:
  # http://jquerytools.github.io/documentation/overlay/
  ###

  # Obtain overlay options from html button attributes.
  options = $.parseJSON($(button).attr('data_overlay'))
  options['subtype'] = 'ajax'
  config = {}
  # overlay.OnLoad javascript snippet

  config['onLoad'] = ->
    triggerid = '[rel=\'#' + @getTrigger().attr('id') + '\']'
    # If there are defined some jsControllers, they'll be reloaded every time the overlay is loaded.
    jscontrollers = $(triggerid).attr('data_jscontrollers')
    jscontrollers = $.parseJSON(jscontrollers)
    if jscontrollers.length > 0
      window.bika.lims.loadControllers false, jscontrollers
    # Check personalized onLoad functionalities.
    handler = $(triggerid).attr('data_overlay_handler')
    if handler != ''
      fn = window[handler]
      if typeof fn == 'function'
        handler = new fn
        if typeof handler.onLoad == 'function'
          handler.onLoad this
    return

  # overlay.OnBeforeClose javascript snippet

  config['onBeforeClose'] = ->
    triggerid = '[rel=\'#' + @getTrigger().attr('id') + '\']'
    handler = $(triggerid).attr('data_overlay_handler')
    if handler != ''
      fn = window[handler]
      if typeof fn == 'function'
        handler = new fn
        if typeof handler.onBeforeClose == 'function'
          handler.onBeforeClose this
          # Done, exit
          return true
    retfields = $.parseJSON($(triggerid).attr('data_returnfields'))
    if retfields.length > 0
      # Default behaviour.
      # Set the value from the returnfields to the input
      # and select the first option.
      # This might be improved by finding a way to get the
      # uid of the object created/edited and assign directly
      # the value to the underlaying referencewidget
      retvals = []
      $.each retfields, (index, value) ->
        retval = $('div.overlay #' + value).val()
        if retval != ''
          retvals.push retval
        return
      if retvals.length > 0
        retvals = retvals.join(' ')
        $(triggerid).prev('input').val(retvals).focus()
        setTimeout (->
          $('.cg-DivItem').first().click()
          return
        ), 500
    true

  options['config'] = config
  $(button).prepOverlay options
  return

load_addbutton_overlays = ->

  ###*
  # Add the overlay conditions for the AddButton.
  ###

  $('a.referencewidget-add-button').each (i) ->
    apply_button_overlay '#' + $(this).attr('id')
    return
  return

load_editbutton_overlay = (button) ->

  ###*
  # Given an element (button), show/hide the element depending on its trigger UID.
  # No UID -> No object selected -> Noting to edit -> hide edit
  # Yes UID -> Object selected -> Something to edit -> show edit.
  ###

  element = '#' + $(button).attr('data_fieldid')
  uid = $(element).attr('uid')
  # No UID found -> Hide Edit button
  if !uid or uid == ''
    $(button).hide()
  else
    # UID found -> Show Edit button & update href attribute
    $(button).show()
    # Get object's id
    request_data = 
      catalog_name: 'uid_catalog'
      UID: uid
    window.bika.lims.jsonapi_read request_data, (data) ->
      root_href = $(button).attr('data_baseurl')
      id = data.objects[0].id
      $(button).attr 'href', root_href + '/' + id + '/edit'
      apply_button_overlay button
      return
  return

load_editbutton_overlays = ->

  ###*
  # Add the overlay conditions for the EditButton.
  ###

  $('a.referencewidget-edit-button').each (i) ->
    button = '#' + $(this).attr('id')
    fieldid = '#' + $(this).attr('data_fieldid')
    $(fieldid).bind 'selected blur paste', ->
      `var button`
      button = '#' + $(this).siblings('a.referencewidget-edit-button').attr('id')
      load_editbutton_overlay button
      return
    load_editbutton_overlay button
    return
  return

(($) ->
  $(document).ready ->
    referencewidget_lookups()
    $('.reference_multi_item .deletebtn').live 'click', ->
      fieldName = $(this).attr('fieldName')
      uid = $(this).attr('uid')
      existing_value = $('input[name^=\'' + fieldName + '_uid\']').val()
      # It's true: the value may have been removed already, by another function
      if existing_value
        existing_uids = existing_value.split(',')
        destroy existing_uids, uid
        $('input[name^=\'' + fieldName + '_uid\']').val existing_uids.join(',')
        $('input[name=\'' + fieldName + '\']').attr 'uid', existing_uids.join(',')
        $(this).parent().remove()
      return
    $('.ArchetypesReferenceWidget').bind 'selected blur change', ->
      e = $(this).children('input.referencewidget')
      # multiValued fields always have empty values in the actual input widget:
      multiValued = $(e).attr('multiValued') == '1'
      if e.val() == '' and !multiValued
        fieldName = $(e).attr('name').split(':')[0]
        $(e).attr 'uid', ''
        $('input[name^=\'' + fieldName + '_uid\']').val ''
        $('div[name=\'' + fieldName + '-listing\']').empty()
      return
    save_UID_check()
    check_UID_check()
    load_addbutton_overlays()
    load_editbutton_overlays()
    return
  return
) jQuery
