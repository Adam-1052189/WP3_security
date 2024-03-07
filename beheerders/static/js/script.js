document.getElementById('openMenu').onclick = function () {
    document.getElementById('Menu').style.width = "250px";
}

document.getElementById('closeMenu').onclick = function () {
    document.getElementById('Menu').style.width = "0";
}


function verwijderen(event, inschrijvingId) {
    event.preventDefault();
    if (!confirm("Weet je zeker dat je deze inschrijving wilt verwijderen?")) {
        return;
    }
    const csrfToken = getCookie('csrftoken');
    fetch(`/beheerders/inschrijvingen/verwijder_inschrijving/${inschrijvingId}/`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': csrfToken,
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                document.getElementById(`inschrijving-item-${inschrijvingId}`).remove();
                alert(data.message);
            } else {
                throw new Error(data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('De inschrijving is succesvol verwijderd');
            window.location.reload();
        });
}

document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelectorAll('.verwijder-link').forEach(button => {
        button.addEventListener('click', function (event) {
            verwijderen(event, this.id.replace('verwijder-knop-', ''));
        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}