(function ($) {
    "use strict";

    /*==================================================================
    [ Validación de formulario de login ]
    Este script valida los campos del formulario antes de enviarlo.
    Si algún campo no es válido, muestra un mensaje de error y evita el envío.
    ==================================================================*/

    // Selecciona todos los inputs que requieren validación
    var input = $('.validate-input .input100');

    // Evento al enviar el formulario
    $('.validate-form').on('submit', function () {
        var check = true;

        // Recorre todos los inputs y valida cada uno
        for (var i = 0; i < input.length; i++) {
            if (validate(input[i]) == false) {
                showValidate(input[i]);
                check = false;
            }
        }

        // Si algún campo no es válido, evita el envío
        return check;
    });

    // Elimina el mensaje de error al enfocar el input
    $('.validate-form .input100').each(function () {
        $(this).focus(function () {
            hideValidate(this);
        });
    });

    // Función para validar un input (email o texto)
    function validate(input) {
        // Si es un campo de email, valida el formato
        if ($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if (
                $(input)
                    .val()
                    ?.toString()
                    .trim()
                    .match(
                        /^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/
                    ) == null
            ) {
                return false;
            }
        }
        // Si es otro campo, solo valida que no esté vacío
        else {
            if ($(input).val()?.toString().trim() == '') {
                return false;
            }
        }
        return true;
    }

    // Muestra el mensaje de error visual en el input
    function showValidate(input) {
        var thisAlert = $(input).parent();
        $(thisAlert).addClass('alert-validate');
    }

    // Oculta el mensaje de error visual en el input
    function hideValidate(input) {
        var thisAlert = $(input).parent();
        $(thisAlert).removeClass('alert-validate');
    }

})($);