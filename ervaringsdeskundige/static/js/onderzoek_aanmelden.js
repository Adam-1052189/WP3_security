document.addEventListener("DOMContentLoaded", function () {
    const aanmeldForm = document.getElementById('aanmeldForm');
    const aanmeldButton = document.getElementById("aanmeldButton");
    const deelnameBerichtContainer = document.createElement('div');
    deelnameBerichtContainer.id = 'deelnameBericht';
    deelnameBerichtContainer.style.display = 'none';
    deelnameBerichtContainer.textContent = 'Je neemt deel aan dit onderzoek.';
    document.body.appendChild(deelnameBerichtContainer);

    if (aanmeldButton) {
        aanmeldButton.addEventListener("click", function () {
            const onderzoekId = this.dataset.onderzoekId;
            fetch(`/ervaringsdeskundige/onderzoek/${onderzoekId}/aanmelden/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({'onderzoek_id': onderzoekId})
            })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        aanmeldForm.style.display = 'none';
                        document.getElementById('deelnameBericht').style.display = 'block';
                        alert(data.message);
                    } else {
                        alert(data.message);
                    }
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        });
    }

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
});