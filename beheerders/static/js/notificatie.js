function haalNotificatiesOp() {
    $.ajax({
        url: '/beheerders/api/notificaties/',
        success: function(data) {
            var notificatiesHtml = '';
            for (var i = 0; i < data.length; i++) {
                var notificatie = data[i];
                notificatiesHtml += '<div class="notificatie-item" id="notificatie-' + notificatie.id + '">' +
                                        '<p>' + notificatie.bericht + '</p>' +
                                        (notificatie.onderzoek ? ('<p>Onderzoek: ' + notificatie.onderzoek.titel + '</p>') : '') +
                                        '<button onclick="markeerAlsGelezen(' + notificatie.id + ')" class="markeer-als-gelezen-btn">Markeer als gelezen</button>' +
                                    '</div>';
            }
            $('#notificaties-container').html(notificatiesHtml);
        }
    });
}

$(document).ready(function() {
    haalNotificatiesOp();

    setInterval(haalNotificatiesOp, 30000);
});

function markeerAlsGelezen(notificatieId) {
    $.ajax({
        type: 'POST',
        url: '/beheerders/api/notificaties/' + notificatieId + '/markeer-als-gelezen/',
        success: function() {
            $('#notificatie-' + notificatieId).remove();
        },
        error: function(xhr, status, error) {
            console.log("Er is een fout opgetreden: " + error);
        }
    });
}