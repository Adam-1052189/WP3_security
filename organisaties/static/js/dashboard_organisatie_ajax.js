$(document).ready(function() {
    function updateOnderzoeken() {
        var ajaxUrl = $('body').data('ajax-url');
        $.ajax({
            url: ajaxUrl,
            type: "GET",
            dataType: "html",
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            success: function(response) {
                $("#onderzoeken-lijst").html(response);
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    }

    setInterval(updateOnderzoeken, 5000);
});