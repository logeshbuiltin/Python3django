function injectTrim(handler) {
    return function(element, event) {
        if (element.tagName === 'TEXTAREA' || (element.tagName === 'INPUT' && element.type !== 'password' && element
        .type !== 'file')) {
            element.value = $.trim(element.value);
        }
        return handler.call(this, element, event);
    };
}

$.validator.addMethod('regex', function(value, element, regexp) {
    var re = new RegExp(regexp);
    return this.optional(element) || re.test(value);
});

$.validator.addMethod('exactlength', function(value, element, param) {
    return this.optional(element) || value.length == param;;
});

$.validator.addMethod('cannotExceed', function(value, element, param) {
    return this.optional(element) || value.length < param;;
});

$.validator.addMethod('dropdown', function(value, element) {
    return !(value === '-Select One-' || value === '-None-' || (value === null));
});


$.validator.addMethod("lesserThan", function (value, element, param) {
          var $otherElement = $(param);
          return parseFloat(parseFloat(value).toFixed(2)) >= parseFloat(parseFloat($otherElement.val()).toFixed(2));
});

var validators = []
$('form:not([method=GET])').each(function() {
        // set current form validator instance to access it from docready
        validators.push($(this).validate({
        debug: false,
        onfocusout: injectTrim(function(element) {
            var elementId = element.getAttribute('id');
            if ($(element).hasClass("datepickerWidget")) {
                // datepicker widget - don't do validation on focusout event
                return false;
            }
            this.element(element);
        }),
        rules: {
            name: {
                required: true,
                regex: /^[a-zA-Z\s]+$/,
            },
            manufacture_name: {
                required: true,
                regex: /^[a-zA-Z0-9\s]+$/,
            },
            model: {
                required: true,
                regex: /^[a-zA-Z0-9\s]+$/,
            },
            confirm_password:{
                required: true,
                equalTo: '#txtPassword'
            },
            consignor_place:{
                required: true,
                dropdown: true
            },
            consignee_place:{
                required: true,
                dropdown: true
            },
            consignor:{
                required: true,
                dropdown: true
            },
            consignee:{
                required: true,
                dropdown: true
            },
            gstin: {
                required: true,
                regex: /^[a-zA-Z0-9]+('|-|)[a-zA-Z0-9\s]*$/,
                exactlength: 15,
            },
            consignor_gst: {
                required: true,
                regex: /^[a-zA-Z0-9]+('|-|)[a-zA-Z0-9\s]*$/,
                exactlength: 15,
            },
            consignee_gst: {
                required: true,
                regex: /^[a-zA-Z0-9]+('|-|)[a-zA-Z0-9\s]*$/,
                exactlength: 15,
            },
            contact_number: {
                required: true,
                exactlength: 10
            },
            family_contact: {
                required: false,
                exactlength: 10
            },
            alternate_contact: {
                required: true,
                exactlength: 10
            },
            no_of_packages: {
                required: true,
            },
            license_number: {
                regex: /^[a-zA-Z0-9\s]+$/,
                cannotExceed: 20,
            },
            license_document:{
                required: true,
                extension: "pdf|img|png|jpg|jpeg"
            },
            freight_charges:{
                required: true
            },
            lr_charges:{
                required: false
            },
            hamali_charges:{
                required: false
            },
            door_collection:{
                required: false
            },
            door_delivery:{
                required: false
            },
            other_charges:{
                required: false
            },
            total_charges:{
                required: true
            },
            place_of_delivery:{
                required: true,
                dropdown: true
            },
            mileage: {
                required: false
            },
            truck_number: {
                regex: /^[a-zA-Z0-9\s]+$/,
            },
            truck_type:{
                required: true
            },
            package_value: {
                required: false
            },
            invoice_no: {
                regex: /^[a-zA-Z0-9\s]+$/,
            },
            charged_weight: {
                lesserThan: '#id_actual_weight'
            },
            no_of_wheels: {
                required: false
            }
        },
        messages: {
            name: {
                regex: "Please enter a valid name"
            },
            manufacture_name:{
                regex: "Please enter a valid name"
            },
            model:{
                regex: "Please enter a valid model"
            },
            confirm_password:{
                equalTo: "Passwords dont match"
            },
            gstin: {
                required: 'Please enter the gst number.',
                regex: 'Please enter a valid consignor gst number.',
                exactlength: "GST Length should be exactly 15"
            },
            contact_number: {
                exactlength: "Invalid Contact"
            },
            family_contact: {
                exactlength: "Invalid Contact"
            },
            alternate_contact: {
                exactlength: "Invalid Contact"
            },
            consignor_gst: {
                required: 'Please enter the gst number.',
                regex: 'Please enter a valid consignor gst number.',
                exactlength: "GST Length should be exactly 15"
            },
            consignee_gst: {
                required: 'Please enter the gst number.',
                regex: 'Please enter a valid consignor gst number.',
                exactlength: "GST Length should be exactly 15"
            },
            license_number:{
                regex: "Please Enter a Valid License Number",
                cannotExceed: "License Number cannot exceed 20 characters"
            },
            license_document:{
                required: "Please upload the License",
                extension: "Please upload a valid file"
            },
            truck_number: {
                regex: "Please enter a valid Truck No"
            },
            invoice_no: {
                regex: "Please enter a valid Invoice No"
            },
            charged_weight: {
                lesserThan: "Charged Weight should be greater than or equal to Actual Weight"
            }
        },
        errorClass: 'error help-block',
        errorPlacement: function(error, element) {
            var elementName = element.attr('name') || element.attr('name');
            var elementId = element.attr('id');
            var e = $(element);
            var errorLabel = $('[for=' + elementName + ']:not(label)');
            e.closest('.form-group').find(errorLabel).html(error.html()).closest('.help-block').css('color','red');
            e.closest('.panel').find(errorLabel).html(error.html()).closest('.help-block').css('display','block');
        },
        success: function (label) {
        },
        highlight: function(element, errorClass) {
            var e = $(element);
            var elementName = e.attr('name') || e.attr('name');
            e.closest('.has-feedback').removeClass('has-success').addClass('has-error');
            var errorLabel = $('[for=' + elementName + ']:not(label)');
            errorLabel.parents('.help-block').show();
            errorLabel.show();
            var feedbackBlock = errorLabel.parents('.has-feedback');
            feedbackBlock.removeClass('has-success').addClass('has-error');
            var feedbackIcon = e.nextAll('.form-control-feedback');
            if (!feedbackIcon.length) {
                feedbackIcon = e.parents().nextAll('.form-control-feedback');
            }
            feedbackIcon.addClass('show').find('i').removeClass('fa-check').addClass('fa-close');
            // If this is an element inside an accordion (which for us here is an element with a `data-target` attribute),
            // expand the enclosing accordion.
            if (e.attr('data-target')) {
                e.parents('.collapse').collapse('show');
                e.parents('.collapse').siblings('.panel-heading').addClass('has-error').removeClass('has-success');
            }

        },
        unhighlight: function(element, errorClass) {
            var e = $(element);
            var elementName = e.attr('name') || e.attr('name');
            $('[for=' + elementName + ']:not(label)').empty().hide();
            e.siblings('small.help-block').empty().hide();
            var feedbackBlock = e.closest('.has-feedback');
            feedbackBlock.removeClass('has-error').addClass('has-success').find('.help-block').hide();
            var feedbackIcon = e.nextAll('.form-control-feedback');
            if (!feedbackIcon.length) {
                feedbackIcon = e.parents().nextAll('.form-control-feedback');
            }
            feedbackIcon.addClass('show').find('i').removeClass('fa-close').addClass('fa-check');
            if (e.attr('data-target')) {
                e.parents('.collapse').siblings('.panel-heading').removeClass('has-error').addClass('has-success');
            }
        },
        submitHandler: function(form) {
         // Manually validate MultiWidgets.
         var groupBoxes = $('[name]');
         if (groupBoxes && groupBoxes.length) {
            groupBoxes.trigger('blur').trigger('focus').valid();
         }
         var forms = $('form:not([method=GET])');
         // Now validate each sub-form.
         var subForms = forms.children('[data-subform]');
         if (subForms && subForms.length) {
            // Form has sub-forms. Validate everything and allow submit only when customer is on last page.
            var currentStep = subForms.filter(':visible');
            var stepId = currentStep.attr('id');
            var step = parseInt(stepId.split('_')[1]);
            // Don't submit if not on last sub-form.
            if (step !== subForms.length) {
                forms.validate().settings.ignore = ':hidden, [readonly]';
                return;
            } else {
                // On last form. Also validate the hidden-inside-accordion fields.
                forms.validate().settings.ignore = ':hidden :not(input[data-target]:hidden), [readonly]';
                // Once ignore rules are changed, manually call validate once again.
                var isValid = forms.valid();
                if (!isValid) {
                    return;
                }
            }
         } else {
            // Form doesn't have sub-forms. Validate hidden-inside-accordion fields.
            forms.validate().settings.ignore = ':hidden :not(input[data-target]:hidden), [readonly]';
            var isValid = forms.valid();
            if (!isValid) {
                return;
            }
         }

         // in  React combine application page remove disabled attribute before submit.
         $( ":disabled" ).each(function() {
            $(this).removeAttr("disabled");
          });

         // Disable button and add a spinner thingy to it.
         var button = $('input[type=submit]');
         button.attr('disabled', true).children('.spinner').removeClass('hide');
         button.children('.icon-lock').addClass(' hide');
         form.submit();
         // Disable other buttons in the same page
         var otherButton = $('[type=button]');
         otherButton.attr('disabled', true);
    }
}))

});

