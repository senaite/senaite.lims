### Please use this command to compile this file into the parent `js` directory:
    coffee --no-header -w -o ../js -c bika.lims.site.coffee

    SENAITE Changes:
      - portal message
###

window.SiteView = ->
  that = this

  loadClientEvents = ->
    # Client creation overlay
    $('a.add_client').prepOverlay
      subtype: 'ajax'
      filter: 'head>*,#content>*:not(div.configlet),dl.portalMessage.error,dl.portalMessage.info'
      formselector: '#client-base-edit'
      closeselector: '[name="form.button.cancel"]'
      width: '70%'
      noform: 'close'
      config:
        closeOnEsc: false
        onLoad: ->
          # manually remove remarks
          @getOverlay().find('#archetypes-fieldname-Remarks').remove()
          return
        onClose: ->
          # here is where we'd populate the form controls, if we cared to.
          return
    # Client combogrid searches by ID
    $('input[id*=\'ClientID\']').combogrid
      colModel: [
        {
          'columnName': 'ClientUID'
          'hidden': true
        }
        {
          'columnName': 'ClientID'
          'width': '20'
          'label': _('Client ID')
        }
        {
          'columnName': 'Title'
          'width': '80'
          'label': _('Title')
        }
      ]
      showOn: true
      width: '450px'
      url: window.portal_url + '/getClients?_authenticator=' + $('input[name="_authenticator"]').val()
      select: (event, ui) ->
        $(this).val ui.item.ClientID
        $(this).change()
        false
    # Display add Client button next to Client ID input for all
    # views except from Client View
    if $('.portaltype-client').length == 0
      $('input[id=\'ClientID\']').after '<a style="border-bottom:none !important;margin-left:.5;"' + ' class="add_client"' + ' href="' + window.portal_url + '/clients/portal_factory/Client/new/edit"' + ' rel="#overlay">' + ' <img style="padding-bottom:1px;" src="' + window.portal_url + '/++resource++bika.lims.images/add.png"/>' + '</a>'
    # Confirm before resetting client specs to default lab specs
    $('a[href*=\'set_to_lab_defaults\']').click (event) ->
      # always prevent default/
      # url is activated manually from 'Yes' below.
      url = $(this).attr('href')
      event.preventDefault()
      y = _('Yes')
      n = _('No')
      $confirmation = $('<div></div>').html(_('This will remove all existing client analysis specifications ' + 'and create copies of all lab specifications. ' + 'Are you sure you want to do this?')).dialog(
        resizable: false
        title: _('Set to lab defaults')
        buttons:
          y: (event) ->
            $(this).dialog 'close'
            window.location.href = url
            return
          n: (event) ->
            $(this).dialog 'close'
            return
      )
      return
    return

  loadReferenceDefinitionEvents = ->
    # a reference definition is selected from the dropdown
    # (../../skins/bika/bika_widgets/referenceresultswidget.js)
    $('#ReferenceDefinition\\:list').change ->
      authenticator = $('input[name="_authenticator"]').val()
      uid = $(this).val()
      option = $(this).children(':selected').html()
      if uid == ''
        # No reference definition selected;
        # render empty widget.
        $('#Blank').prop 'checked', false
        $('#Hazardous').prop 'checked', false
        $('.bika-listing-table').load 'referenceresults', '_authenticator': authenticator
        return
      if option.search(_('(Blank)')) > -1
        $('#Blank').prop 'checked', true
      else
        $('#Blank').prop 'checked', false
      if option.search(_('(Hazardous)')) > -1
        $('#Hazardous').prop 'checked', true
      else
        $('#Hazardous').prop 'checked', false
      $('.bika-listing-table').load 'referenceresults',
        '_authenticator': authenticator
        'uid': uid
      return
    # If validation failed, and user is returned to page - requires reload.
    if $('#ReferenceDefinition\\:list').val() != ''
      $('#ReferenceDefinition\\:list').change()
    return

  loadCommonEvents = ->
    curDate = new Date
    y = curDate.getFullYear()
    limitString = '1900:' + y
    dateFormat = _('date_format_short_datepicker')

    split = (val) ->
      val.split /,\s*/

    extractLast = (term) ->
      split(term).pop()

    stop_spinner = ->
      counter--
      if counter < 0
        counter = 0
      if counter == 0
        clearTimeout timer
        spinner.stop()
        spinner.hide()
      return

    if dateFormat == 'date_format_short_datepicker'
      dateFormat = 'yy-mm-dd'
    $('input.datepicker').live 'click', ->
      $(this).datepicker(
        showOn: 'focus'
        showAnim: ''
        changeMonth: true
        changeYear: true
        dateFormat: dateFormat
        yearRange: limitString).click(->
        $(this).attr 'value', ''
        return
      ).focus()
      return

    ###*
    This function defines a datepicker for a date range. Both input
    elements should be siblings and have the class 'date_range_start' and
    'date_range_end'.
    ###

    $('input.datepicker_range').datepicker
      showOn: 'focus'
      showAnim: ''
      changeMonth: true
      changeYear: true
      dateFormat: dateFormat
      yearRange: limitString
    $('input.datepicker_nofuture').live 'click', ->
      $(this).datepicker(
        showOn: 'focus'
        showAnim: ''
        changeMonth: true
        changeYear: true
        maxDate: curDate
        dateFormat: dateFormat
        yearRange: limitString).click(->
        $(this).attr 'value', ''
        return
      ).focus()
      return
    $('input.datepicker_2months').live 'click', ->
      $(this).datepicker(
        showOn: 'focus'
        showAnim: ''
        changeMonth: true
        changeYear: true
        maxDate: '+0d'
        numberOfMonths: 2
        dateFormat: dateFormat
        yearRange: limitString).click(->
        $(this).attr 'value', ''
        return
      ).focus()
      return
    $('input.datetimepicker_nofuture').live 'click', ->
      $(this).datetimepicker(
        showOn: 'focus'
        showAnim: ''
        changeMonth: true
        changeYear: true
        maxDate: curDate
        dateFormat: dateFormat
        yearRange: limitString
        timeFormat: 'HH:mm'
        beforeShow: ->
          setTimeout (->
            $('.ui-datepicker').css 'z-index', 99999999999999
            return
          ), 0
          return
      ).click(->
        $(this).attr 'value', ''
        return
      ).focus()
      return
    # Analysis Service popup trigger
    $('.service_title span:not(.before)').live 'click', ->
      dialog = $('<div></div>')
      dialog.load(window.portal_url + '/analysisservice_popup',
        'service_title': $(this).closest('td').find('span[class^=\'state\']').html()
        'analysis_uid': $(this).parents('tr').attr('uid')
        '_authenticator': $('input[name=\'_authenticator\']').val()).dialog
        width: 450
        height: 450
        closeText: _('Close')
        resizable: true
        title: $(this).text()
      return
    $('.numeric').live 'paste', (event) ->
      # Wait (next cycle) for value popluation and replace commas.
      $self = $(this)
      window.setTimeout (->
        $self.val $self.val().replace(',', '.')
        return
      ), 0
      return
    $('.numeric').live 'keypress', (event) ->
      allowedKeys = [
        8
        9
        13
        35
        36
        37
        39
        46
        44
        60
        62
        45
        69
        101
        61
      ]
      isAllowedKey = allowedKeys.join(',').match(new RegExp(event.which))
      # IE doesn't support indexOf
      # Some browsers just don't raise events for control keys. Easy. e.g. Safari backspace.
      if !event.which or 48 <= event.which and event.which <= 57 or isAllowedKey
        # Opera assigns values for control keys.
        # Wait (next cycle) for value popluation and replace commas.
        $self = $(this)
        window.setTimeout (->
          $self.val $self.val().replace(',', '.')
          return
        ), 0
        return
      else
        event.preventDefault()
      return
    # autocomplete input controller
    availableTags = $.parseJSON($('input.autocomplete').attr('voc'))
    $('input.autocomplete').on('keydown', (event) ->
      if event.keyCode == $.ui.keyCode.TAB and $(this).autocomplete('instance').menu.active
        event.preventDefault()
      return
    ).autocomplete
      minLength: 0
      source: (request, response) ->
        # delegate back to autocomplete, but extract the last term
        response $.ui.autocomplete.filter(availableTags, extractLast(request.term))
        return
      focus: ->
        # prevent value inserted on focus
        false
      select: (event, ui) ->
        terms = split(@value)
        # remove the current input
        terms.pop()
        # add the selected item
        terms.push ui.item.value
        # add placeholder to get the comma-and-space at the end
        terms.push ''
        @value = terms.join(', ')
        false
    # Archetypes :int and IntegerWidget inputs get filtered
    $('input[name*=\'\\:int\'], .ArchetypesIntegerWidget input').keyup (e) ->
      if /\D/g.test(@value)
        @value = @value.replace(/\D/g, '')
      return
    # Archetypes :float and DecimalWidget inputs get filtered
    $('input[name*=\'\\:float\'], .ArchetypesDecimalWidget input').keyup (e) ->
      if /[^-.\d]/g.test(@value)
        @value = @value.replace(/[^-.\d]/g, '')
      return

    ### Replace kss-bbb spinner with a quieter one ###

    timer = undefined
    spinner = undefined
    counter = 0
    $(document).unbind 'ajaxStart'
    $(document).unbind 'ajaxStop'
    $('#ajax-spinner').remove()
    spinner = $('<div id="bika-spinner"><img src="' + portal_url + '/spinner.gif" alt=""/></div>')
    spinner.appendTo('body').hide()
    $(document).ajaxStart ->
      counter++
      setTimeout (->
        if counter > 0
          spinner.show 'fast'
        return
      ), 500
      return
    $(document).ajaxStop ->
      stop_spinner()
      return
    $(document).ajaxError (event, jqxhr, settings, thrownError) ->
      stop_spinner()
      window.bika.lims.log 'Error at ' + settings.url + ': ' + thrownError
      return
    return

  portalAlert = (html) ->
    if $('#portal-alert').length == 0
      $('#portal-header').append "<div id='portal-alert' style='display:none'><div class='portal-alert-item alert'>#{html}</div></div>"
    else
      $('#portal-alert').append "<div class='portal-alert-item alert'>#{html}</div>"
    $('#portal-alert').fadeIn()
    return

  loadFilterByDepartment = ->

    ###*
    This function sets up the filter by department cookie value by chosen departments.
    Also it does auto-submit if admin wants to enable/disable the department filtering.
    ###

    $('#department_filter_submit').click ->
      if !$('#admin_dep_filter_enabled').is(':checked')
        deps = []
        $.each $('input[name^=chb_deps_]:checked'), ->
          deps.push $(this).val()
          return
        cookiename = 'filter_by_department_info'
        if deps.length == 0
          deps.push $('input[name^=chb_deps_]:checkbox:not(:checked):visible:first').val()
        createCookie cookiename, deps.toString()
      location.reload()
      return
    $('#admin_dep_filter_enabled').change ->
      cookiename = 'filter_by_department_info'
      if $(this).is(':checked')
        deps = []
        $.each $('input[name^=chb_deps_]:checkbox'), ->
          deps.push $(this).val()
          return
        createCookie cookiename, deps
        createCookie 'dep_filter_disabled', 'true'
        location.reload()
      else
        createCookie 'dep_filter_disabled', 'false'
        location.reload()
      return
    loadFilterByDepartmentCookie()
    return

  loadFilterByDepartmentCookie = ->

    ###*
    This function checks if the cookie 'filter_by_department_info' is
    available. If the cookie exists, do nothing, if the cookie has not been
    created yet, checks the selected department in the checkbox group and creates the cookie with the UID of the first department.
    If cookie value "dep_filter_disabled" is true, it means the user is admin and filtering is disabled.
    ###

    # Gettin the cookie
    cookiename = 'filter_by_department_info'
    cookie_val = readCookie(cookiename)
    if cookie_val == null or document.cookie.indexOf(cookiename) < 1
      dep_uid = $('input[name^=chb_deps_]:checkbox:visible:first').val()
      createCookie cookiename, dep_uid
    dep_filter_disabled = readCookie('dep_filter_disabled')
    if dep_filter_disabled == 'true' or dep_filter_disabled == '"true"'
      $('#admin_dep_filter_enabled').prop 'checked', true
    return

  ###*
  This function updates the minimum selectable date of date_range_end
  @param {object} input_element is the <input> object for date_range_start
  ###

  date_range_controller_0 = (input_element) ->
    date_element = $(input_element).datepicker('getDate')
    brother = $(input_element).siblings('.date_range_end')
    $(brother).datepicker 'option', 'minDate', date_element
    return

  ###*
  This function updates the maximum selectable date of date_range_start
  @param {object} input_element is the <input> object for date_range_end
  ###

  date_range_controller_1 = (input_element) ->
    date_element = $(input_element).datepicker('getDate')
    brother = $(input_element).siblings('.date_range_start')
    $(brother).datepicker 'option', 'maxDate', date_element
    return

  that.load = ->
    loadCommonEvents()
    loadClientEvents()
    loadReferenceDefinitionEvents()
    loadFilterByDepartment()
    #Date range controllers
    $('.date_range_start').bind 'change', ->
      date_range_controller_0 this
      return
    $('.date_range_end').bind 'change', ->
      date_range_controller_1 this
      return
    return

  that.notificationPanel = (data, mode) ->

    ###*
    # Render an alert inside the content panel. Used for autosave in ARView, for example.
    ###

    $('#panel-notification').remove()
    $('div#viewlet-above-content-title').append '<div id=\'panel-notification\' style=\'display:none\'>' + '<div class=\'' + mode + '-notification-item\'>' + data + '</div></div>'
    $('#panel-notification').fadeIn 'slow', 'linear', ->
      setTimeout (->
        $('#panel-notification').fadeOut 'slow', 'linear'
        return
      ), 3000
      return
    return

  return
