function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function afkeuren(event, onderzoekId) {
    event.preventDefault();
    const csrfToken = getCookie('csrftoken');

    fetch(`/beheerders/onderzoeksvragen/afkeuren/${onderzoekId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
    if (data.status === 'success') {

        const afkeurKnop = document.getElementById(`afkeur-knop-${onderzoekId}`);
        if (afkeurKnop) {
            afkeurKnop.style.display = 'none';
        }

        document.getElementById(`status-${onderzoekId}`).innerText = 'Afgekeurd';

        alert(data.message);
        window.location.reload();
    } else {
        throw new Error(data.message);
    }
})
.catch(error => {
    console.error('Error:', error);
    alert('Er is een fout opgetreden: ' + error.message);
});
}


function goedkeuren(event, onderzoekId) {
    event.preventDefault();
    const csrfToken = getCookie('csrftoken');

    fetch(`/beheerders/onderzoeksvragen/goedkeuren/${onderzoekId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
    if (data.status === 'success') {

        const afkeurKnop = document.getElementById(`goedkeur-knop-${onderzoekId}`);
        if (afkeurKnop) {
            afkeurKnop.style.display = 'none';
        }

        document.getElementById(`status-${onderzoekId}`).innerText = 'Goedgekeurd';

        alert(data.message)
        window.location.reload();
    } else {
        throw new Error(data.message);
    }
})
.catch(error => {
    console.error('Error:', error);
    alert('Er is een fout opgetreden: ' + error.message);
});
}