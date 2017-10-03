
/* Please use this command to compile this file into the parent `js` directory:
    coffee --no-header -w -o ../js -c spotlight.coffee

    The JS will be integrated in templates/spotlight_viewlet.pt
 */

(function() {
  var base,
    extend = function(child, parent) { for (var key in parent) { if (hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; },
    hasProp = {}.hasOwnProperty,
    bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };

  if (window.app == null) {
    window.app = {};
  }

  if ((base = window.app).spotlight == null) {
    base.spotlight = {};
  }

  $(document).ready(function() {
    var ResultView, ResultsView, SearchResult, SearchResults, SearchView, Spotlight, SpotlightController;
    Spotlight = (function() {
      function Spotlight() {
        var me;
        this.map = {};
        this.document = $(document);
        this.spotlight = $("#spotlight");
        this.overlay = this.spotlight.overlay({
          onLoad: function(event) {
            var el;
            console.debug("***spotlight_overlay.onLoad***");
            el = $(event.target);
            $("#spotlight-search-field", el).focus();
            return el.draggable();
          },
          mask: {
            color: 'black',
            opacity: '0.6'
          }
        });
        me = this;
        this.document.on("keydown keyup", function(event) {
          return me.onSpotlightKey(event);
        });
        $("#spotlight-trigger a").on("click", function(event) {
          console.debug("Spotlight trigger button clicked");
          event.preventDefault();
          if (document.URL.endsWith("spotlight")) {
            return $("#spotlight-search-field", me.spotlight).focus();
          } else {
            return me.spotlightOverlay();
          }
        });
        $(".spotlight-overlay #spotlight-clear-button").on("click", function(event) {
          console.log("Clear button of the overlay clicked");
          event.preventDefault();
          return me.spotlightOverlay();
        });
      }

      Spotlight.prototype.spotlightOverlay = function() {
        if (document.URL.endsWith("spotlight")) {
          console.debug("Spotlight overlay disabled on spotlight view");
          return true;
        }
        if (this.overlay.isOpened == null) {
          this.overlay = this.overlay.overlay();
        }
        if (this.overlay.isOpened()) {
          return this.overlay.close();
        } else {
          return this.overlay.load();
        }
      };

      Spotlight.prototype.onSpotlightKey = function(event) {
        var code;
        code = event.keyCode;
        if (code !== 17 && code !== 32) {
          return;
        }
        this.map[code] = event.type === 'keydown';
        if (this.map[17] && this.map[32]) {
          console.debug("Ctrl-Space detected -> Trigger Spotlight");
          return this.spotlightOverlay();
        }
      };

      return Spotlight;

    })();
    window.app.spotlight.spotlight = new Spotlight();

    /* MODELS */
    SearchResult = (function(superClass) {
      extend(SearchResult, superClass);

      function SearchResult() {
        return SearchResult.__super__.constructor.apply(this, arguments);
      }

      SearchResult.prototype.defaults = {
        id: "",
        title: "",
        url: "",
        icon: "",
        state: "",
        title_or_id: ""
      };

      return SearchResult;

    })(Backbone.Model);
    SearchResults = (function(superClass) {
      extend(SearchResults, superClass);

      function SearchResults() {
        return SearchResults.__super__.constructor.apply(this, arguments);
      }

      SearchResults.prototype.model = SearchResult;

      return SearchResults;

    })(Backbone.Collection);

    /* VIEWS */
    ResultView = (function(superClass) {
      extend(ResultView, superClass);

      function ResultView() {
        return ResultView.__super__.constructor.apply(this, arguments);
      }

      ResultView.prototype.tagName = "tr";

      ResultView.prototype.template = underscore.template($('#item-template').html());

      ResultView.prototype.render = function() {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
      };

      return ResultView;

    })(Backbone.View);
    ResultsView = (function(superClass) {
      extend(ResultsView, superClass);

      function ResultsView() {
        this.render = bind(this.render, this);
        return ResultsView.__super__.constructor.apply(this, arguments);
      }

      ResultsView.prototype.tagName = "table";

      ResultsView.prototype.className = "table";

      ResultsView.prototype.id = "search-results";

      ResultsView.prototype.template = underscore.template($('#results-template').html());

      ResultsView.prototype.initialize = function() {
        return this.collection.bind("results:changed", this.render);
      };

      ResultsView.prototype.render = function() {
        this.$el.html(this.template(this.collection.toJSON()));
        this.collection.each(function(result, index) {
          return this.addResult(result, index);
        }, this);
        return this;
      };

      ResultsView.prototype.addResult = function(model, index) {
        var className, view;
        className = index % 2 === 0 ? "even" : "odd";
        view = new ResultView({
          model: model,
          className: className
        });
        return this.$el.append(view.render().el);
      };

      return ResultsView;

    })(Backbone.View);
    SearchView = (function(superClass) {
      extend(SearchView, superClass);

      function SearchView() {
        this.onKeyup = bind(this.onKeyup, this);
        this.onClear = bind(this.onClear, this);
        return SearchView.__super__.constructor.apply(this, arguments);
      }

      SearchView.prototype.el = "#spotlight";

      SearchView.prototype.initialize = function() {
        return this.resultsView != null ? this.resultsView : this.resultsView = new ResultsView({
          collection: this.collection
        });
      };

      SearchView.prototype.events = {
        "keyup #spotlight-search-field": "onKeyup",
        "click #spotlight-clear-button": "onClear"
      };

      SearchView.prototype.onClear = function(event) {
        event.preventDefault();
        this.$("#spotlight-search-field").val("");
        return this.trigger("query:changed", "");
      };

      SearchView.prototype.onKeyup = function(event) {
        var code, value;
        code = event.keyCode || event.which;
        if (code === 13 || code === 38 || code === 40) {
          event.preventDefault();
          event.stopPropagation();
          return this.selectRow(event);
        }
        value = this.$("#spotlight-search-field").val();
        return this.trigger("query:changed", value);
      };

      SearchView.prototype.selectRow = function(event) {
        var active, code, href, next, results, table;
        code = event.keyCode;
        table = $(".spotlight-overlay #search-results");
        results = $("tbody tr", table);
        if (!(results.length > 0)) {
          return;
        }
        active = $("tr.selected", table);
        if (active.length === 0) {
          results.first().addClass("selected");
          return true;
        }
        if (code === 38) {
          next = active.prev();
        } else if (code === 40) {
          next = active.next();
        } else if (code === 13) {
          href = $("a.link", active).attr("href");
          console.log("Navigate to " + href);
          location.href = href;
          return true;
        }
        active.removeClass("selected");
        next.addClass("selected");
        return true;
      };

      SearchView.prototype.render = function() {
        return this.$("#search-results-wrapper").html(this.resultsView.el);
      };

      return SearchView;

    })(Backbone.View);

    /* CONTROLLERS */
    SpotlightController = (function(superClass) {
      extend(SpotlightController, superClass);

      function SpotlightController() {
        this.search = bind(this.search, this);
        return SpotlightController.__super__.constructor.apply(this, arguments);
      }

      SpotlightController.prototype.el = $("#spotlight");

      SpotlightController.prototype.initialize = function() {
        console.debug("SpotlightController initialized");
        if (this.searchResults == null) {
          this.searchResults = new SearchResults();
        }
        if (this.searchView == null) {
          this.searchView = new SearchView({
            collection: this.searchResults
          });
        }
        this.searchView.render();
        this.lazySearch = underscore.debounce(this.search, 500);
        return this.searchView.bind("query:changed", this.lazySearch);
      };

      SpotlightController.prototype.search = function(query) {
        var q, url;
        this.searchResults.reset();
        url = "@@API/spotlight/search";
        q = {
          q: query,
          limit: 10
        };
        return $.getJSON(url, q, (function(_this) {
          return function(data) {
            underscore.each(data.items, function(result, index) {
              var searchResult;
              searchResult = new SearchResult(result);
              return this.searchResults.add(searchResult);
            }, _this);
            return _this.searchResults.trigger("results:changed");
          };
        })(this));
      };

      return SpotlightController;

    })(Backbone.View);
    return window.app.spotlight.SpotlightController = new SpotlightController();
  });

}).call(this);
