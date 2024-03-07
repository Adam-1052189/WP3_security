document.addEventListener("DOMContentLoaded", function () {
    const aanmeldForm = document.getElementById('aanmeldForm');
    const aanmeldButton = document.getElementById("aanmeldButton");
    const annuleerButton = document.getElementById("annuleerButton");
    const deelnameBerichtContainer = document.getElementById('deelnameBericht') || document.createElement('div');

    if (!document.getElementById('deelnameBericht')) {
        deelnameBerichtContainer.id = 'deelnameBericht';
        deelnameBerichtContainer.style.display = 'none';
        deelnameBerichtContainer.textContent = 'Je neemt deel aan dit onderzoek.';
        document.body.appendChild(deelnameBerichtContainer);
    }

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
                        deelnameBerichtContainer.style.display = 'block';
                        annuleerButton.style.display = 'block';
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

    if (annuleerButton) {
        annuleerButton.addEventListener("click", function () {
            const onderzoekId = this.dataset.onderzoekId;
            console.log('Annuleringsverzoek verzonden voor onderzoek ID:', onderzoekId);
            fetch(`/ervaringsdeskundige/onderzoek/${onderzoekId}/annuleren/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    }
                    throw new Error('Netwerkantwoord was niet ok.');
                })
                .then(data => {
                    console.log('Antwoord:', data);
                    if (data.success) {
                        deelnameBerichtContainer.style.display = 'none';
                        aanmeldForm.style.display = 'block';
                        annuleerButton.style.display = 'none';
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
