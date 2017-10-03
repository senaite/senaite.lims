### Please use this command to compile this file into the parent `js` directory:
    coffee --no-header -w -o ../js -c spotlight.coffee

    The JS will be integrated in templates/spotlight_viewlet.pt
###
window.app ?= {}
window.app.spotlight ?= {}

$(document).ready ->

  class Spotlight
    constructor: ->
      @map = {}
      @document = $(document)
      @spotlight = $("#spotlight")

      # configure the overlay
      @overlay = @spotlight.overlay
        onLoad: (event) ->
          console.debug "***spotlight_overlay.onLoad***"
          el = $(event.target)
          $("#spotlight-search-field", el).focus()
          el.draggable()
        mask:
          color: 'black'
          opacity: '0.6'

      me = this

      @document.on "keydown keyup", (event) ->
        me.onSpotlightKey(event)

      # The spotlight button in the nav-bar
      $("#spotlight-trigger a").on "click", (event) ->
        console.debug "Spotlight trigger button clicked"
        event.preventDefault()
        if document.URL.endsWith "spotlight"
          $("#spotlight-search-field", me.spotlight).focus()
        else
          me.spotlightOverlay()

      $(".spotlight-overlay #spotlight-clear-button").on "click", (event) ->
        console.log "Clear button of the overlay clicked"
        event.preventDefault()
        me.spotlightOverlay()

    spotlightOverlay: ->
      if document.URL.endsWith "spotlight"
        console.debug "Spotlight overlay disabled on spotlight view"
        return yes
      # XXX: why?
      if not @overlay.isOpened?
        @overlay = @overlay.overlay()
      if @overlay.isOpened()
        @overlay.close()
      else
        @overlay.load()

    onSpotlightKey: (event) ->
      code = event.keyCode
      return unless code in [17, 32]
      @map[code] = event.type is 'keydown'
      if @map[17] and @map[32]
        console.debug "Ctrl-Space detected -> Trigger Spotlight"
        @spotlightOverlay()

  window.app.spotlight.spotlight = new Spotlight()


  ### MODELS ###

  # Single search result
  class SearchResult extends Backbone.Model
    defaults:
      id: ""
      title: ""
      url: ""
      icon: ""
      state: ""
      title_or_id: ""

  # Collection of search results
  class SearchResults extends Backbone.Collection
    model: SearchResult


  ### VIEWS ###

  # Renders a single search result
  class ResultView extends Backbone.View
    tagName: "tr"
    template: underscore.template $('#item-template').html()

    render: ->
      @$el.html @template @model.toJSON()
      return @


  # Renders all search results
  class ResultsView extends Backbone.View
    tagName: "table"
    className: "table"
    id: "search-results"

    template: underscore.template $('#results-template').html()

    initialize: ->
      # this is triggered when a new set of results is loaded into the collection.
      @collection.bind "results:changed", @render

    render: =>
      @$el.html @template @collection.toJSON()
      # @$el.attr "style", "width:100%"

      @collection.each (result, index) ->
        @addResult result, index
      , this

      return @

    addResult: (model, index) ->
      className = if index % 2 == 0 then "even" else "odd"
      view = new ResultView model: model, className: className
      @$el.append view.render().el


  # The search view wraps all other views below and does not render itself
  class SearchView extends Backbone.View
    el: "#spotlight"

    initialize: ->
      # all results will be rendered by this view
      @resultsView ?= new ResultsView collection: @collection

    events:
      "keyup #spotlight-search-field": "onKeyup"
      "click #spotlight-clear-button": "onClear"

    onClear: (event) =>
      event.preventDefault()
      @$("#spotlight-search-field").val("")
      @trigger "query:changed", ""

    onKeyup: (event) =>
      # special key handling
      code = event.keyCode or event.which
      if code in [13, 38, 40]
        event.preventDefault()
        event.stopPropagation()
        return @selectRow event
      value = @$("#spotlight-search-field").val()
      @trigger "query:changed", value

    selectRow: (event) ->
      code = event.keyCode
      table = $(".spotlight-overlay #search-results")
      results = $("tbody tr", table)

      # Nothing to select, because we have no results
      return unless results.length > 0

      # search for selected rows in the search results
      active = $("tr.selected", table)

      # Nothing selected so far, choose the first row
      if active.length == 0
        results.first().addClass "selected"
        return true

      # KEY UP
      if code == 38
        next = active.prev()

      # KEY DOWN
      else if code is 40
        next = active.next()

      # ENTER
      else if code is 13
        href = $("a.link", active).attr("href")
        console.log "Navigate to #{href}"
        location.href = href
        return true

      # deselect the current active row
      active.removeClass "selected"
      # select the next possible row
      next.addClass "selected"

      return true

    render: ->
      # render the results view table into the search-results-wrapper
      @$("#search-results-wrapper").html @resultsView.el


  ### CONTROLLERS ###

  class SpotlightController extends Backbone.View
    el: $("#spotlight")

    initialize: ->
      console.debug "SpotlightController initialized"

      # The holding collection for all search results
      @searchResults ?= new SearchResults()

      # Initialize a single search view and pass in the collection instance.
      # Backbone will take care that his will be accessbile as `this.collection`
      # on the view
      @searchView ?= new SearchView collection: @searchResults

      # render the main view
      @searchView.render()

      # debounce the search to avoid request flooding
      @lazySearch = underscore.debounce @search, 500

      # The view notifies us when the user entered something in the search field
      @searchView.bind "query:changed", @lazySearch


    # Executest the search and adds the results to the collection
    search: (query) =>
      # reset the collection
      @searchResults.reset()

      # URL to query
      url = "@@API/spotlight/search"

      # prepare  the query
      q = q: query, limit: 10

      # execute the search
      $.getJSON url, q, (data) =>
        underscore.each data.items, (result, index) ->
          searchResult = new SearchResult(result)
          # add the new search result to the collection
          @searchResults.add searchResult
        , this
        # trigger finished event
        @searchResults.trigger "results:changed"

  window.app.spotlight.SpotlightController = new SpotlightController()
