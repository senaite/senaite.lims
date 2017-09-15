###* Helper JS to change classnames and HTML on the fly
 *
 * Please use this command to compile this file into the parent `js` directory:
 *
 * coffee --no-header -w -o ../js -c bootstrap-integration.coffee
###

$(document).ready ->
  console.log '** SENAITE BOOTSTRAP INTEGRATION **'

  # https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver
  observer = new MutationObserver (mutations) ->
    $.each mutations, (index, record) ->
      # watch added nodes
      $.each record.addedNodes, (index, el) ->
        $(document).trigger "onCreate", el

  # Observe the document.body for future added elements
  observer.observe document.body,
    childList: yes
    subtree: yes

  # some on-the-fly modificaitons on dynamically created elements
  $(document).on "onCreate", (event, el) ->
    $el = $(el)
    if $el.hasClass "tooltip"
      fix_bika_listing_tooltip el

  # onCreate event handler
  fix_bika_listing_tooltip = (el) ->
    console.debug "Fix listing table tooltip"
    $el = $(el)
    $el.addClass "bottom bika-tooltip"
    $el.wrapInner "<div class='tooltip-inner'></div>"
    $el.append "<div class='tooltip-arrow'></div>"

  # Show new loader on Ajax events
  $(document).on
    ajaxStart: ->
      $('body').addClass 'loading'
      $('.modal').show()
      return
    ajaxStop: ->
      $('body').removeClass 'loading'
      $('.modal').hide()
      return
    ajaxError: ->
      $('body').removeClass 'loading'
      $('.modal').hide()
      return

  # Remove default Bika spinner (Replaced with the modal spinner above)
  $('bika-spinner').remove()

  # Remove inline styles in headlines
  $('h1>span').attr 'style', ''

  # Convert form-tabs to navigation pills
  $('ul.formTabs').addClass 'nav nav-pills'
  # Form tabbing
  $('ul.formTabs li').on "click", ->
    $(this).parent().children().removeClass "active"
    $(this).addClass "active"

  # AR Add Form
  $('table.ar-table td [fieldname]').addClass 'form-inline'

  # Worksheets
  $('.worksheet_add_controls').addClass 'form-inline'

  # Data Grid Field
  $('.datagridwidget-add-button').addClass 'btn btn-default'

  # Add button CSS classes to form buttons
  $('input[type="submit"], input[type="button"]').addClass 'btn btn-default'

  # Add table CSS classes
  $('table').addClass 'table table-condensed table-bordered table-striped'

  # Convert all 'hiddenStructure' classes to 'hidden'
  $('.hiddenStructure').addClass 'hidden'
  $('.template-manage-viewlets .hide').removeClass 'hide'
  $('.template-manage-viewlets .show').removeClass 'show'
  hiddenviewlet = $('<span>This viewlet is hidden and will not be shown</span>')
  $(hiddenviewlet).addClass 'text-danger'
  $('.template-manage-viewlets .hiddenViewlet').prepend hiddenviewlet

  ### Form customizations ###
  $('form').addClass 'form'
  $('input').addClass 'input-sm'
  $('form input[type=text]').addClass 'form-control'
  $('form input[type=password]').addClass 'form-control'
  $('form textarea').addClass 'form-control'
  $('form select').addClass 'form-control'
  $('form textarea').attr 'rows', 10
  $('form div.formQuestion').removeClass 'label'
  $('div.plone_jscalendar').addClass 'form-inline'

  # Text format selector for RichText fields
  $('.fieldTextFormat').addClass('form-inline').addClass 'pull-right'

  # Make the portal_messages redish in case of error
  $('.alert-error').removeClass('alert-error').addClass 'alert-danger'
  # fix portal messages
  mapping =
    "error": "danger"
  $('dl.portalMessage').each ->
    $el = $(this)
    $el.removeClass 'portalMessage'
    cls = $el[0].className
    title = $el.find("dt").html()
    message = $el.find("dd").html()
    facility = mapping[cls] if cls of mapping or cls
    replacement = $("""
      <div data-alert='alert' class='alert alert-dismissible alert-#{facility}'>
        <button type='button' class='close' data-dismiss='alert' aria-label='Close'>
          <span aria-hidden='true'>×</span>
        </button>
        <strong>#{title}</strong>
        <p>#{message}</p>
      </div>
    """)
    replacement.attr "style", $el.attr("style")
    $el.replaceWith replacement

  # Manage Portlets Link
  $('.managePortletsLink a').addClass 'btn btn-default btn-xs'

  # Help text in Archetypes forms
  $('.formHelp').addClass('help-block').removeClass 'formHelp'

  # Plone Control Panel
  $('div#edit-bar ul').addClass 'nav nav-tabs'
  $('div#edit-bar ul li.selected').addClass 'active'
  $('a#setup-link').addClass 'btn btn-default'
  $('div.field').addClass 'form-group'

  # Plone Add-on Panel
  $('#content-core ul.configlets').addClass 'nav nav-stacked well'
  $('.portletItem ul.configlets').addClass 'nav'

  # Convert input[type=buttons] to button tags
  foundPrimary = false
  $('div.formControls input[type="submit"]').each ->
    input = $(this)
    button = $('<button type="submit" class="btn btn-sm btn-default" name="' + input.attr('name') + '"value="' + input.attr('value') + '">' + input.attr('value') + '</button>')
    if input.hasClass('context') and !foundPrimary
      button.addClass 'btn-primary'
      foundPrimary = true
    input.replaceWith button
    return
