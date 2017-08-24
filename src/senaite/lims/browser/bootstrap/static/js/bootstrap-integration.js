/*
 * Helper JS to change classnames and HTML on the fly
 * because it would be too hard to do it customizing
 * each template
 *
 */

function fixArchetypesForms(){
    /* Remove class=label from datetime widgets */
    $('.ArchetypesCalendarWidget .label').each(function(){
        var cont = $(this).contents().filter(function(){
            return this.nodeType == 3 && $(this).text().trim();
        }).wrap('<label></label>');

    });

    /* Move archetypes BooleanFields' checkbox, inside the label */
    $('.ArchetypesBooleanWidget label').each(function(){
        var checkbox = $(this).parent().find('input[type=checkbox]');
        $(this).prepend(checkbox);
        $(this).removeClass('label');
    });

    $('.ArchetypesSelectionWidget label').each(function(){
        var radio = $(this).prev();
        if ($(radio).attr("type")=='radio'){
            $(this).prepend(radio);
        }
    });


    $('.ArchetypesSelectionWidget .formQuestion.label').each(
        function(){
            $(this).removeClass('label');
        }
    );

    /* Move add-on control-panel inputs inside labels*/
    $('input[type=checkbox]').each(function(){
        var label = $(this).parent().find('label');
        for (var i = label.length - 1; i >= 0; i--) {
            if ($(label[i]).attr('for') == $(this).attr('id')) {
                if ($(label[i]).hasClass('hiddenStructure')) {
                    var labeltext = $(label[i]).text();
                    $(label[i]).text('');
                    $(label[i]).removeClass('hiddenStructure');
                    $(label[i]).prepend($("<span />", { 'class': 'hiddenStructure', 'text': labeltext}));

                }
                $(label[i]).prepend($(this));
                var span = $(label[i]).find('span');
                span.removeClass('label');
            }

        };

    });

    $('form.edit-form .label').removeClass('label');

    /* Help text in Archetypes forms */
    $('.formHelp').addClass('help-block').removeClass('formHelp');
}

$(document).ready(function(){
    console.log("** SENAITE BOOTSTRAP INTEGRATION **");

    /* LOADER */
    $(document).on({
        ajaxStart: function() {
            $("body").addClass("loading");
            $(".modal").show();
        },
        ajaxStop: function() {
            $("body").removeClass("loading");
            $(".modal").hide();
        },
        ajaxError: function() {
            $("body").removeClass("loading");
            $(".modal").hide();
        }
    });

    /* Bika LIMS Customizations */

    // remove all inline styles in headlines
    $("h1>span").attr("style", "");

    /* Form tabbing */
    $("ul.formTabs").addClass("nav nav-pills");

    $('div.field').addClass('form-group');

    /* /Bika LIMS Customizations */

    /* Convert input[type=buttons] to button tags */
    var foundPrimary = false;
    $('div.formControls input[type="submit"]').each(function(){
        var input = $(this);
        var button = $('<button type="submit" class="btn btn-xs btn-default" name="' + input.attr('name') + '"value="' + input.attr('value') + '">' +
                       input.attr('value') + '</button>');

        if(input.hasClass('context') && !foundPrimary){
            button.addClass('btn-primary');
            foundPrimary = true;
        }
        input.replaceWith(button);
    });

    /* Convert DGF Buttons */
    $(".datagridwidget-add-button").addClass("btn btn-default");

    /* Add btn class to the rest form buttons */
    $('input[type="submit"], input[type="button"]').addClass('btn btn-xs btn-default');

    /* Plone's default class for tables */
    // $('table').not('.bika-listing-table').addClass('table table-condensed table-bordered table-striped');
    $('table').addClass('table table-condensed table-bordered table-striped');

    /* Fix archetypes forms if there's any */
    fixArchetypesForms();

    /* Convert all 'hiddenStructure' classes to 'hidden' */
    $('.hiddenStructure').addClass('hidden');

    $('.template-manage-viewlets .hide').removeClass('hide');
    $('.template-manage-viewlets .show').removeClass('show');
    var hiddenviewlet = $('<span>This viewlet is hidden and will not be shown</span>');
    $(hiddenviewlet).addClass('text-danger');
    $('.template-manage-viewlets .hiddenViewlet').prepend(hiddenviewlet);

    /* forms */
    $('form').addClass('form');
    $('form input[type=text]').addClass('form-control').addClass('input-sm');
    $('form input[type=password]').addClass('form-control');
    $('form textarea').addClass('form-control input-sm');
    $('form select').addClass('form-control input-sm');
    $('form textarea').attr('rows', 10);

    /* login form */
    $('.template-login_form').addClass('form-inline');

    /* Date fields */
    $('#fieldset-dates').addClass('form-inline');
    $('.date-field').parent().addClass('form-inline');

    /* Content-tree input */
    $('.autocompleteInputWidget').on('DOMSubtreeModified', function(){
        $('.autocompleteInputWidget .option .label').removeClass('label');
    });

    $('.fieldErrorBox').each(function(){
        if ($(this).text() != "") {
            $(this).parent().addClass('has-error');
            $(this).wrapInner('<span class="text-danger"></span>');
        }
    });

    /* Text format selector for RichText fields */
    $('.fieldTextFormat').addClass('form-inline').addClass('pull-right');

    /* Make the portal_messages redish in case of error */
    $('.alert-error').removeClass('alert-error').addClass('alert-danger');
});
