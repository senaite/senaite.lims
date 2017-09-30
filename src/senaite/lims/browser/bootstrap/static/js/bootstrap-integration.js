
/** Helper JS to change classnames and HTML on the fly
 *
 * Please use this command to compile this file into the parent `js` directory:
 *
 * coffee --no-header -w -o ../js -c bootstrap-integration.coffee
 */

(function() {
  $(document).ready(function() {
    var fix_bika_listing_tooltip, foundPrimary, hiddenviewlet, mapping, observer;
    console.log('** SENAITE BOOTSTRAP INTEGRATION **');
    observer = new MutationObserver(function(mutations) {
      return $.each(mutations, function(index, record) {
        return $.each(record.addedNodes, function(index, el) {
          return $(document).trigger("onCreate", el);
        });
      });
    });
    observer.observe(document.body, {
      childList: true,
      subtree: true
    });
    $(document).on("onCreate", function(event, el) {
      var $el;
      $el = $(el);
      if ($el.hasClass("tooltip")) {
        return fix_bika_listing_tooltip(el);
      }
    });
    fix_bika_listing_tooltip = function(el) {
      var $el;
      console.debug("Fix listing table tooltip");
      $el = $(el);
      $el.addClass("bottom bika-tooltip");
      $el.wrapInner("<div class='tooltip-inner'></div>");
      return $el.append("<div class='tooltip-arrow'></div>");
    };
    $(document).on({
      ajaxStart: function() {
        $('body').addClass('loading');
        $('.modal').show();
      },
      ajaxStop: function() {
        $('body').removeClass('loading');
        $('.modal').hide();
      },
      ajaxError: function() {
        $('body').removeClass('loading');
        $('.modal').hide();
      }
    });
    $('bika-spinner').remove();
    $('h1>span').attr('style', '');
    $('ul.formTabs').addClass('nav nav-pills');
    $('ul.formTabs li').on("click", function() {
      $(this).parent().children().removeClass("active");
      return $(this).addClass("active");
    });
    $('table.ar-table td [fieldname]').addClass('form-inline');
    $('.worksheet_add_controls').addClass('form-inline');
    $('.datagridwidget-add-button').addClass('btn btn-default');
    $('input[type="submit"], input[type="button"]').addClass('btn btn-default');
    $('table').addClass('table table-condensed table-bordered table-striped');
    $('.hiddenStructure').addClass('hidden');
    $('.template-manage-viewlets .hide').removeClass('hide');
    $('.template-manage-viewlets .show').removeClass('show');
    hiddenviewlet = $('<span>This viewlet is hidden and will not be shown</span>');
    $(hiddenviewlet).addClass('text-danger');
    $('.template-manage-viewlets .hiddenViewlet').prepend(hiddenviewlet);

    /* Form customizations */
    $('form').addClass('form');
    $('input').addClass('input-sm');
    $('form input[type=text]').addClass('form-control');
    $('form input[type=password]').addClass('form-control');
    $('form textarea').addClass('form-control');
    $('form select').addClass('form-control');
    $('form textarea').attr('rows', 10);
    $('form div.formQuestion').removeClass('label');
    $('div.plone_jscalendar').addClass('form-inline');
    $('.fieldTextFormat').addClass('form-inline').addClass('pull-right');
    $('.alert-error').removeClass('alert-error').addClass('alert-danger');
    mapping = {
      "error": "danger"
    };
    $('dl.portalMessage').each(function() {
      var $el, cls, facility, message, replacement, title;
      $el = $(this);
      $el.removeClass('portalMessage');
      cls = $el[0].className;
      title = $el.find("dt").html();
      message = $el.find("dd").html();
      if (cls in mapping || cls) {
        facility = mapping[cls];
      }
      replacement = $("<div data-alert='alert' class='alert alert-dismissible alert-" + facility + "'>\n  <button type='button' class='close' data-dismiss='alert' aria-label='Close'>\n    <span aria-hidden='true'>×</span>\n  </button>\n  <strong>" + title + "</strong>\n  <p>" + message + "</p>\n</div>");
      replacement.attr("style", $el.attr("style"));
      return $el.replaceWith(replacement);
    });
    $('.managePortletsLink a').addClass('btn btn-default btn-xs');
    $('.formHelp').addClass('help-block').removeClass('formHelp');
    $('div#edit-bar ul').addClass('nav nav-tabs');
    $('div#edit-bar ul li.selected').addClass('active');
    $('a#setup-link').addClass('btn btn-default');
    $('div.field').addClass('form-group');
    $('#content-core ul.configlets').addClass('nav nav-stacked well');
    $('.portletItem ul.configlets').addClass('nav');
    foundPrimary = false;
    return $('div.formControls input[type="submit"]').each(function() {
      var button, input;
      input = $(this);
      button = $('<button type="submit" class="btn btn-sm btn-default" name="' + input.attr('name') + '"value="' + input.attr('value') + '">' + input.attr('value') + '</button>');
      if (input.hasClass('context') && !foundPrimary) {
        button.addClass('btn-primary');
        foundPrimary = true;
      }
      input.replaceWith(button);
    });
  });

}).call(this);
