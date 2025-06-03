
(function ($) {
    "use strict";

     $('tbody tr[data-href]').css('cursor', 'pointer').on('click', function () {
        window.location = $(this).data('href');
    });

})(jQuery);