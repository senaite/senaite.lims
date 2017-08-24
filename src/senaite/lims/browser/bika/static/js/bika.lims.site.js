
/* Please use this command to compile this file into the parent `js` directory:
    coffee --no-header -w -o ../js -c bika.lims.site.coffee

    SENAITE Changes:
      - portal message
 */

(function() {
  window.SiteView = function() {
    var date_range_controller_0, date_range_controller_1, loadClientEvents, loadCommonEvents, loadFilterByDepartment, loadFilterByDepartmentCookie, loadReferenceDefinitionEvents, portalAlert, that;
    that = this;
    loadClientEvents = function() {
      $('a.add_client').prepOverlay({
        subtype: 'ajax',
        filter: 'head>*,#content>*:not(div.configlet),dl.portalMessage.error,dl.portalMessage.info',
        formselector: '#client-base-edit',
        closeselector: '[name="form.button.cancel"]',
        width: '70%',
        noform: 'close',
        config: {
          closeOnEsc: false,
          onLoad: function() {
            this.getOverlay().find('#archetypes-fieldname-Remarks').remove();
          },
          onClose: function() {}
        }
      });
      $('input[id*=\'ClientID\']').combogrid({
        colModel: [
          {
            'columnName': 'ClientUID',
            'hidden': true
          }, {
            'columnName': 'ClientID',
            'width': '20',
            'label': _('Client ID')
          }, {
            'columnName': 'Title',
            'width': '80',
            'label': _('Title')
          }
        ],
        showOn: true,
        width: '450px',
        url: window.portal_url + '/getClients?_authenticator=' + $('input[name="_authenticator"]').val(),
        select: function(event, ui) {
          $(this).val(ui.item.ClientID);
          $(this).change();
          return false;
        }
      });
      if ($('.portaltype-client').length === 0) {
        $('input[id=\'ClientID\']').after('<a style="border-bottom:none !important;margin-left:.5;"' + ' class="add_client"' + ' href="' + window.portal_url + '/clients/portal_factory/Client/new/edit"' + ' rel="#overlay">' + ' <img style="padding-bottom:1px;" src="' + window.portal_url + '/++resource++bika.lims.images/add.png"/>' + '</a>');
      }
      $('a[href*=\'set_to_lab_defaults\']').click(function(event) {
        var $confirmation, n, url, y;
        url = $(this).attr('href');
        event.preventDefault();
        y = _('Yes');
        n = _('No');
        $confirmation = $('<div></div>').html(_('This will remove all existing client analysis specifications ' + 'and create copies of all lab specifications. ' + 'Are you sure you want to do this?')).dialog({
          resizable: false,
          title: _('Set to lab defaults'),
          buttons: {
            y: function(event) {
              $(this).dialog('close');
              window.location.href = url;
            },
            n: function(event) {
              $(this).dialog('close');
            }
          }
        });
      });
    };
    loadReferenceDefinitionEvents = function() {
      $('#ReferenceDefinition\\:list').change(function() {
        var authenticator, option, uid;
        authenticator = $('input[name="_authenticator"]').val();
        uid = $(this).val();
        option = $(this).children(':selected').html();
        if (uid === '') {
          $('#Blank').prop('checked', false);
          $('#Hazardous').prop('checked', false);
          $('.bika-listing-table').load('referenceresults', {
            '_authenticator': authenticator
          });
          return;
        }
        if (option.search(_('(Blank)')) > -1) {
          $('#Blank').prop('checked', true);
        } else {
          $('#Blank').prop('checked', false);
        }
        if (option.search(_('(Hazardous)')) > -1) {
          $('#Hazardous').prop('checked', true);
        } else {
          $('#Hazardous').prop('checked', false);
        }
        $('.bika-listing-table').load('referenceresults', {
          '_authenticator': authenticator,
          'uid': uid
        });
      });
      if ($('#ReferenceDefinition\\:list').val() !== '') {
        $('#ReferenceDefinition\\:list').change();
      }
    };
    loadCommonEvents = function() {
      var availableTags, counter, curDate, dateFormat, extractLast, limitString, spinner, split, stop_spinner, timer, y;
      curDate = new Date;
      y = curDate.getFullYear();
      limitString = '1900:' + y;
      dateFormat = _('date_format_short_datepicker');
      split = function(val) {
        return val.split(/,\s*/);
      };
      extractLast = function(term) {
        return split(term).pop();
      };
      stop_spinner = function() {
        var counter;
        counter--;
        if (counter < 0) {
          counter = 0;
        }
        if (counter === 0) {
          clearTimeout(timer);
          spinner.stop();
          spinner.hide();
        }
      };
      if (dateFormat === 'date_format_short_datepicker') {
        dateFormat = 'yy-mm-dd';
      }
      $('input.datepicker').live('click', function() {
        $(this).datepicker({
          showOn: 'focus',
          showAnim: '',
          changeMonth: true,
          changeYear: true,
          dateFormat: dateFormat,
          yearRange: limitString
        }).click(function() {
          $(this).attr('value', '');
        }).focus();
      });

      /**
      This function defines a datepicker for a date range. Both input
      elements should be siblings and have the class 'date_range_start' and
      'date_range_end'.
       */
      $('input.datepicker_range').datepicker({
        showOn: 'focus',
        showAnim: '',
        changeMonth: true,
        changeYear: true,
        dateFormat: dateFormat,
        yearRange: limitString
      });
      $('input.datepicker_nofuture').live('click', function() {
        $(this).datepicker({
          showOn: 'focus',
          showAnim: '',
          changeMonth: true,
          changeYear: true,
          maxDate: curDate,
          dateFormat: dateFormat,
          yearRange: limitString
        }).click(function() {
          $(this).attr('value', '');
        }).focus();
      });
      $('input.datepicker_2months').live('click', function() {
        $(this).datepicker({
          showOn: 'focus',
          showAnim: '',
          changeMonth: true,
          changeYear: true,
          maxDate: '+0d',
          numberOfMonths: 2,
          dateFormat: dateFormat,
          yearRange: limitString
        }).click(function() {
          $(this).attr('value', '');
        }).focus();
      });
      $('input.datetimepicker_nofuture').live('click', function() {
        $(this).datetimepicker({
          showOn: 'focus',
          showAnim: '',
          changeMonth: true,
          changeYear: true,
          maxDate: curDate,
          dateFormat: dateFormat,
          yearRange: limitString,
          timeFormat: 'HH:mm',
          beforeShow: function() {
            setTimeout((function() {
              $('.ui-datepicker').css('z-index', 99999999999999);
            }), 0);
          }
        }).click(function() {
          $(this).attr('value', '');
        }).focus();
      });
      $('.service_title span:not(.before)').live('click', function() {
        var dialog;
        dialog = $('<div></div>');
        dialog.load(window.portal_url + '/analysisservice_popup', {
          'service_title': $(this).closest('td').find('span[class^=\'state\']').html(),
          'analysis_uid': $(this).parents('tr').attr('uid'),
          '_authenticator': $('input[name=\'_authenticator\']').val()
        }).dialog({
          width: 450,
          height: 450,
          closeText: _('Close'),
          resizable: true,
          title: $(this).text()
        });
      });
      $('.numeric').live('paste', function(event) {
        var $self;
        $self = $(this);
        window.setTimeout((function() {
          $self.val($self.val().replace(',', '.'));
        }), 0);
      });
      $('.numeric').live('keypress', function(event) {
        var $self, allowedKeys, isAllowedKey;
        allowedKeys = [8, 9, 13, 35, 36, 37, 39, 46, 44, 60, 62, 45, 69, 101, 61];
        isAllowedKey = allowedKeys.join(',').match(new RegExp(event.which));
        if (!event.which || 48 <= event.which && event.which <= 57 || isAllowedKey) {
          $self = $(this);
          window.setTimeout((function() {
            $self.val($self.val().replace(',', '.'));
          }), 0);
          return;
        } else {
          event.preventDefault();
        }
      });
      availableTags = $.parseJSON($('input.autocomplete').attr('voc'));
      $('input.autocomplete').on('keydown', function(event) {
        if (event.keyCode === $.ui.keyCode.TAB && $(this).autocomplete('instance').menu.active) {
          event.preventDefault();
        }
      }).autocomplete({
        minLength: 0,
        source: function(request, response) {
          response($.ui.autocomplete.filter(availableTags, extractLast(request.term)));
        },
        focus: function() {
          return false;
        },
        select: function(event, ui) {
          var terms;
          terms = split(this.value);
          terms.pop();
          terms.push(ui.item.value);
          terms.push('');
          this.value = terms.join(', ');
          return false;
        }
      });
      $('input[name*=\'\\:int\'], .ArchetypesIntegerWidget input').keyup(function(e) {
        if (/\D/g.test(this.value)) {
          this.value = this.value.replace(/\D/g, '');
        }
      });
      $('input[name*=\'\\:float\'], .ArchetypesDecimalWidget input').keyup(function(e) {
        if (/[^-.\d]/g.test(this.value)) {
          this.value = this.value.replace(/[^-.\d]/g, '');
        }
      });

      /* Replace kss-bbb spinner with a quieter one */
      timer = void 0;
      spinner = void 0;
      counter = 0;
      $(document).unbind('ajaxStart');
      $(document).unbind('ajaxStop');
      $('#ajax-spinner').remove();
      spinner = $('<div id="bika-spinner"><img src="' + portal_url + '/spinner.gif" alt=""/></div>');
      spinner.appendTo('body').hide();
      $(document).ajaxStart(function() {
        counter++;
        setTimeout((function() {
          if (counter > 0) {
            spinner.show('fast');
          }
        }), 500);
      });
      $(document).ajaxStop(function() {
        stop_spinner();
      });
      $(document).ajaxError(function(event, jqxhr, settings, thrownError) {
        stop_spinner();
        window.bika.lims.log('Error at ' + settings.url + ': ' + thrownError);
      });
    };
    portalAlert = function(html) {
      if ($('#portal-alert').length === 0) {
        $('#portal-header').append("<div id='portal-alert' style='display:none'><div class='portal-alert-item alert'>" + html + "</div></div>");
      } else {
        $('#portal-alert').append("<div class='portal-alert-item alert'>" + html + "</div>");
      }
      $('#portal-alert').fadeIn();
    };
    loadFilterByDepartment = function() {

      /**
      This function sets up the filter by department cookie value by chosen departments.
      Also it does auto-submit if admin wants to enable/disable the department filtering.
       */
      $('#department_filter_submit').click(function() {
        var cookiename, deps;
        if (!$('#admin_dep_filter_enabled').is(':checked')) {
          deps = [];
          $.each($('input[name^=chb_deps_]:checked'), function() {
            deps.push($(this).val());
          });
          cookiename = 'filter_by_department_info';
          if (deps.length === 0) {
            deps.push($('input[name^=chb_deps_]:checkbox:not(:checked):visible:first').val());
          }
          createCookie(cookiename, deps.toString());
        }
        location.reload();
      });
      $('#admin_dep_filter_enabled').change(function() {
        var cookiename, deps;
        cookiename = 'filter_by_department_info';
        if ($(this).is(':checked')) {
          deps = [];
          $.each($('input[name^=chb_deps_]:checkbox'), function() {
            deps.push($(this).val());
          });
          createCookie(cookiename, deps);
          createCookie('dep_filter_disabled', 'true');
          location.reload();
        } else {
          createCookie('dep_filter_disabled', 'false');
          location.reload();
        }
      });
      loadFilterByDepartmentCookie();
    };
    loadFilterByDepartmentCookie = function() {

      /**
      This function checks if the cookie 'filter_by_department_info' is
      available. If the cookie exists, do nothing, if the cookie has not been
      created yet, checks the selected department in the checkbox group and creates the cookie with the UID of the first department.
      If cookie value "dep_filter_disabled" is true, it means the user is admin and filtering is disabled.
       */
      var cookie_val, cookiename, dep_filter_disabled, dep_uid;
      cookiename = 'filter_by_department_info';
      cookie_val = readCookie(cookiename);
      if (cookie_val === null || document.cookie.indexOf(cookiename) < 1) {
        dep_uid = $('input[name^=chb_deps_]:checkbox:visible:first').val();
        createCookie(cookiename, dep_uid);
      }
      dep_filter_disabled = readCookie('dep_filter_disabled');
      if (dep_filter_disabled === 'true' || dep_filter_disabled === '"true"') {
        $('#admin_dep_filter_enabled').prop('checked', true);
      }
    };

    /**
    This function updates the minimum selectable date of date_range_end
    @param {object} input_element is the <input> object for date_range_start
     */
    date_range_controller_0 = function(input_element) {
      var brother, date_element;
      date_element = $(input_element).datepicker('getDate');
      brother = $(input_element).siblings('.date_range_end');
      $(brother).datepicker('option', 'minDate', date_element);
    };

    /**
    This function updates the maximum selectable date of date_range_start
    @param {object} input_element is the <input> object for date_range_end
     */
    date_range_controller_1 = function(input_element) {
      var brother, date_element;
      date_element = $(input_element).datepicker('getDate');
      brother = $(input_element).siblings('.date_range_start');
      $(brother).datepicker('option', 'maxDate', date_element);
    };
    that.load = function() {
      loadCommonEvents();
      loadClientEvents();
      loadReferenceDefinitionEvents();
      loadFilterByDepartment();
      $('.date_range_start').bind('change', function() {
        date_range_controller_0(this);
      });
      $('.date_range_end').bind('change', function() {
        date_range_controller_1(this);
      });
    };
    that.notificationPanel = function(data, mode) {

      /**
       * Render an alert inside the content panel. Used for autosave in ARView, for example.
       */
      $('#panel-notification').remove();
      $('div#viewlet-above-content-title').append('<div id=\'panel-notification\' style=\'display:none\'>' + '<div class=\'' + mode + '-notification-item\'>' + data + '</div></div>');
      $('#panel-notification').fadeIn('slow', 'linear', function() {
        setTimeout((function() {
          $('#panel-notification').fadeOut('slow', 'linear');
        }), 3000);
      });
    };
  };

}).call(this);
