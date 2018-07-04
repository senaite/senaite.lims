###* Helper JS to change classnames and HTML on the fly
 *
 * Please use this command to compile this file into the parent `js` directory:
 *
 * coffee --no-header -w -o ../js -c bootstrap-integration.coffee
###

class Bootstrap
  ###
   * Bootstrap Fixtures for SENAITE
  ###

  constructor: ->
    # Remove default Bika spinner (Replaced with the modal spinner above)
    $("bika-spinner").remove()

    $("h1").next("p").addClass "text-info"
    $("div.documentDescription").addClass "text-info"

    # Worksheets
    $(".worksheet_add_controls").addClass "form-inline"
    $("td.Pos").css("vertical-align", "top")
    $("td.Pos table.worksheet-position tbody tr").css("border", "none")
    $("td.Pos table.worksheet-position tbody tr td").css("vertical-align", "top")
    $(".bika-listing-table td.result.remarks").parent("tr").children("td").css("border", "none")
    $(".bika-listing-table td.result.remarks").css("padding-left", "23px")

    # Add table CSS classes
    $("table")
    .not(".bika-listing-table-container table")
    .not(".ordered-selection-field")
    .not(".recordswidget")
    .addClass "table table-condensed table-bordered table-striped"

    # Convert all 'hiddenStructure' classes to 'hidden'
    $(".hiddenStructure").addClass "hidden"

    # Make the portal_messages redish in case of error
    $(".alert-error").removeClass("alert-error").addClass "alert-danger"

    # Manage Portlets Link
    $(".managePortletsLink a").addClass "btn btn-default btn-xs"

    # Plone Add-on Panel
    $("#content-core ul.configlets").addClass "nav nav-stacked well"
    $(".portletItem ul.configlets").addClass "nav"

    $("a#setup-link").addClass "btn btn-link"
    $("a.link-parent").addClass "btn btn-link"

    $("button").not(".navbar-toggle").addClass "btn btn-default"
    $("input[type='submit']").addClass "btn btn-default"

    # Remove the "Add" menu
    $("#plone-contentmenu-factories").remove()
    # Remove the "Display" menu
    $("#plone-contentmenu-display").remove()

    return @


  fix_form: (el) ->
    console.debug "Bootstrap::fix_form"

    $el = $(el)
    if not $el.is "form"
      console.error "Element is not a form"
      return

    $el.addClass "form"
    $el.find("input").not(".bika-listing-table :checkbox").addClass "input-sm"
    # $el.find("input[type=text]").addClass "form-control"
    # $el.find("input[type=password]").addClass "form-control"
    $el.find("select").addClass "input-sm"
    # find seems to not work for textareas
    $("textarea").addClass "form-control"
    $el.find("div.formQuestion").removeClass "label"
    $el.find("div.plone_jscalendar").addClass "form-inline"
    $el.find("span.label").removeClass "label"
    # Help text in Archetypes forms
    $el.find(".formHelp").addClass("help-block small").removeClass "formHelp"
    $el.find("div.field").addClass "form-group"
    # Text format selector for RichText fields
    $el.find(".fieldTextFormat").addClass("form-inline").addClass "pull-right"
    # Add button CSS classes to form buttons
    $el.find("input[type='submit'], input[type='button']").addClass "btn btn-default"
    $el.find("button").addClass "btn btn-default"
    # Data Grid Field
    $el.find(".datagridwidget-add-button").addClass "btn btn-default"

    # Convert input[type=buttons] to button tags
    foundPrimary = false
    $("div.formControls input[type='submit']").each ->
      input = $(this)
      button = $('<button type="submit" class="btn btn-sm btn-default" name="' + input.attr('name') + '"value="' + input.attr('value') + '">' + input.attr('value') + '</button>')
      if input.hasClass("context") and !foundPrimary
        button.addClass "btn-primary"
        foundPrimary = true
      input.replaceWith button


  fix_listing_table: (el) ->
    console.debug "Bootstrap::fix_listing_table"

    $el = $(el)
    if not $el.hasClass "bika-listing-table"
      console.error "Element is not a listing table"
      return

    # $el.find("*[style]").not(".progress-bar").removeAttr("style");
    $el.addClass "table table-condensed table-striped table-responsive"
    $el.find("th.column").addClass("small")
    $el.find("tbody.item-listing-tbody").addClass("small")
    $el.find("td.review_state_selector a").addClass "btn btn-sm btn-default"
    $el.find("span.workflow_action_buttons input").addClass "btn btn-sm btn-default"
    $el.find("td.filter").addClass "text-right"
    $el.find(".filter-search-input").addClass "input-sm"
    $el.find("td.batching").addClass "text-right"
    $el.find("a.bika_listing_show_more").addClass "btn btn-default btn-sm"
    $el.find("select").removeClass "input-sm"


  fix_listing_table_tooltip: (el) ->
    console.debug "Bootstrap::fix_listing_table_tooltip"

    $el = $(el)
    if not $el.hasClass "tooltip"
      console.error "Element is not a listing table tooltip"
      return

    $el = $(el)
    $el.addClass "bottom bika-tooltip"
    $el.wrapInner "<div class='tooltip-inner'></div>"
    $el.append "<div class='tooltip-arrow'></div>"


  fix_portal_message: (el, remove_others=yes) ->
    console.debug "Bootstrap::fix_portal_message"

    $el = $(el)
    if not $el.hasClass "portalMessage"
      console.error "Element is not a portal message"
      return

    mapping =
      "error": "danger"

    if remove_others
      # remove all previous error messages
      $("#viewlet-above-content div[data-alert='alert']").remove()

    $el.removeClass "portalMessage"
    cls = $el[0].className
    title = $el.find("dt").html()
    message = $el.find("dd").html()
    facility = mapping[cls] if cls of mapping or cls
    replacement = $("""
      <div data-alert="alert" class="alert alert-dismissible alert-#{facility}">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
          <span aria-hidden="true">×</span>
        </button>
        <strong>#{title}</strong>
        <p>#{message}</p>
      </div>
    """)
    replacement.attr "style", $el.attr("style")
    $el.replaceWith replacement


  fix_pagination: (el) ->
    console.debug "Bootstrap::fix_pagination"

    $el = $(el)
    if not $el.hasClass "pagination"
      console.error "Element is not a pagination element"
      return

    ul = $("<ul class='pagination'></ul>")
    ul.append $el.children()
    ul.find("a").wrap("<li class='page-item'></li>")
    ul.find("span").wrap("<li class='page-item active'></li>")
    ul.find("a").addClass "page-link"
    $el.replaceWith ul


  fix_header_table: (el) ->
    console.debug "Bootstrap::fix_header_table"

    $el = $(el)
    if not $el.hasClass "header_table"
      console.error "Element is not a header table"
      return

    $el.addClass("table-sm").removeClass("table-striped")
    $el.find("td:first-child()").addClass("active")
    $el.find("td.key").addClass("active")
    $el.find("td").addClass "small"
    $el.find("div.field").removeClass "form-group"


  fix_results_interpretation: (el) ->
    console.debug "Bootstrap::fix_results_interpretation"

    $el = $(el)
    if not $el.hasClass "arresultsinterpretation-container"
      console.error "Element is not a results interpretation container"
      return

    $el.parent().find("input[type='submit']").css("margin", "0.5em 0 0 0").addClass "btn-primary"

    $el.find("ul").addClass("nav nav-tabs")
    @activate_form_tabbing $el


  fix_remarks_field: (el) ->
    console.debug "Bootstrap::fix_remarks_field"

    $el = $(el)

    if $el.attr("id") isnt "archetypes-fieldname-Remarks"
      console.error "Element is not a remarks field"
      return

    $el.css "padding-top", "2em"
    $el.find("fieldset legend").css "margin", "0 0 0 0"
    $el.find("fieldset legend").css "padding", "1em 0 0 0"
    # Remarks text
    remarks = $el.find "fieldset span"
    remarks.find("br").remove()
    remarks.addClass "text-danger"
    remarks.css "font-size", "100%"
    remarks.css "font-weight", "bold"
    remarks.html (index, html) ->
      html.replace /===/g, "<br/>☞"



  fix_manage_viewlets: (el) ->
    console.debug "Bootstrap::fix_manage_viewlets"

    $el = $(el)
    if not $el.hasClass "template-manage-viewlets"
      console.error "Element is not the manage viewlets view"
      return

    $el.find(".hide").removeClass "hide"
    $el.find(".show").removeClass "show"
    hiddenviewlet = $("<span>This viewlet is hidden and will not be shown</span>")
    $(hiddenviewlet).addClass "text-danger"
    $el.find(".hiddenViewlet").prepend hiddenviewlet


  fix_form_tabs: (el) ->
    console.debug "Bootstrap::fix_form_tabs"

    $el = $(el)
    if not $el.is "ul"
      console.error "Element is not a list element"
      return

    # skip dropdown menus
    if $el.hasClass "dropdown-menu"
      return

    # Convert form-tabs to navigation pills
    $el.addClass "nav nav-tabs"
    @activate_form_tabbing $el


  activate_form_tabbing: (el) ->
    console.debug "Bootstrap::activate_form_tabbing"

    $el = $(el)

    # Set the current active tab
    $el.find(".selected").parent("li").addClass "active"

    # activate the first tab
    if $el.find(".active").length == 0
      $el.find("li").first().addClass "active"

    # Handle tab change
    $el.find("li").on "click", ->
      $(this).parent().find("li.active").removeClass "active"
      $(this).addClass "active"


# /BOOTSTRAP


# DOCUMENT READY ENTRYPOINT
$(document).ready ->
  console.log '** SENAITE BOOTSTRAP INTEGRATION **'

  bs = new Bootstrap()
  window.senaite ?= {}
  window.senaite.bootstrap = bs

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

    if $el.text().startsWith "==="
      remarks = $el.closest "#archetypes-fieldname-Remarks"
      if remarks.length > 0
        bs.fix_remarks_field remarks

    if $el.hasClass "tooltip"
      bs.fix_listing_table_tooltip el

    if $el.hasClass("portalMessage")
      bs.fix_portal_message $el

    if $el.hasClass "bika-listing-table"
      bs.fix_listing_table el

    if $el.hasClass "workflow_action_button"
      table = $el.closest "table.bika-listing-table"
      bs.fix_listing_table table

  # Fix all forms
  $("form").each ->
    bs.fix_form this

  # Fix all listing tables
  $("table.bika-listing-table").each ->
    bs.fix_listing_table this

  # Fix all header tables
  $("table.header_table").each ->
    bs.fix_header_table this

  # Fix all Portal messages
  $("dl.portalMessage").each ->
    bs.fix_portal_message this

  # Fix Pagination
  $(".pagination").each ->
    bs.fix_pagination this

  # Fix all results interpretations
  $("div.arresultsinterpretation-container").each ->
    bs.fix_results_interpretation this

  # Fix remarks field
  $("#archetypes-fieldname-Remarks").each ->
    bs.fix_remarks_field this

  # Fix all form tabs
  $("ul.formTabs").each ->
    bs.fix_form_tabs this

  # Fix all editing tabs
  $("div#editing-bar ul").each ->
    bs.fix_form_tabs this

  # Fix all edit tabs (control panel)
  $("div#edit-bar ul").each ->
    bs.fix_form_tabs this

  # Fix manage viewlets
  $(".template-manage-viewlets").each ->
    bs.fix_manage_viewlets this

  # Show new loader on Ajax events
  $(document).on
    ajaxStart: ->
      $("body").addClass "loading"
      $(".modal").show()
      return
    ajaxStop: ->
      $("body").removeClass "loading"
      $(".modal").hide()
      return
    ajaxError: ->
      $("body").removeClass "loading"
      $(".modal").hide()
      return
