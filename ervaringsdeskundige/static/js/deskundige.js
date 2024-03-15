function logoutUser() {
    const logoutUrl = document.querySelector('button[data-logout-url]').getAttribute('data-logout-url');
    fetch(logoutUrl, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert(data.message);
                window.location.href = '';
            } else {
                alert(data.message);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
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

document.addEventListener("DOMContentLoaded", function() {
    function laadOnderzoeken(type) {
        var xhr = new XMLHttpRequest();
        var container = document.getElementById("onderzoeken-container");
        var url = `${container.getAttribute('data-laad-onderzoeken-url')}?type=${type}`;
        xhr.open("GET", url, true);
        xhr.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                container.innerHTML = this.responseText;
                updateTitle(type);
                applySearchFilter();
            }
        };
        xhr.send();
    }

    function updateTitle(type) {
        var titel = document.getElementById("onderzoeken-titel");
        if (type === 'beschikbaar') {
            titel.textContent = 'Beschikbare Onderzoeken';
        } else if (type === 'deelgenomen') {
            titel.textContent = 'Deelgenomen Onderzoeken';
        } else if (type === 'afwachting') {
            titel.textContent = 'Onderzoeken In Afwachting';
        } else if (type === 'afgekeurd') {
            titel.textContent = 'Afgekeurde Onderzoeken';
        }
    }

    function applySearchFilter() {
        const zoekBalk = document.getElementById('zoekbalk');
        if (!zoekBalk) return;

        zoekBalk.addEventListener('input', function() {
            const zoekterm = this.value.toLowerCase();
            const onderzoeken = document.querySelectorAll('.onderzoek-item');

            onderzoeken.forEach(function(item) {
                const titel = item.querySelector('strong') ? item.querySelector('strong').textContent.toLowerCase() : '';
                const omschrijving = item.innerText.toLowerCase();
                if (titel.includes(zoekterm) || omschrijving.includes(zoekterm)) {
                    item.style.display = '';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    }

    document.getElementById("show-beschikbare-onderzoeken").addEventListener("click", function() {
        laadOnderzoeken('beschikbaar');
    });

    document.getElementById("show-afwachting-onderzoeken").addEventListener("click", function() {
        laadOnderzoeken('afwachting');
    });

    document.getElementById("show-deelgenomen-onderzoeken").addEventListener("click", function() {
        laadOnderzoeken('deelgenomen');
    });

    document.getElementById("show-afgekeurde-onderzoeken").addEventListener("click", function() {
        laadOnderzoeken('afgekeurd');
    });


    const existingZoekbalk = document.getElementById('zoekbalk');
    if (!existingZoekbalk) {
        const newZoekbalk = document.createElement('input');
        newZoekbalk.setAttribute('type', 'text');
        newZoekbalk.setAttribute('id', 'zoekbalk');
        newZoekbalk.setAttribute('placeholder', 'Zoek in onderzoeken...');
        newZoekbalk.setAttribute('aria-label', 'Zoek in onderzoeken');
        newZoekbalk.classList.add('zoekbalk');

        const section = document.getElementById("onderzoeken-section");
        section.insertBefore(newZoekbalk, section.firstChild);
    }

    laadOnderzoeken('beschikbaar');
    applySearchFilter();
});
