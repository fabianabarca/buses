// Contact form page JS

// Se hace query del formulario
const formulario = document.querySelector('form');

formulario.addEventListener(
    'submit',
    event => {
        // Se cancela el refresh
        event.preventDefault();

        // Hacemos el post a través de fetch
        fetch("post_form", {
            method: "POST",
            body: new FormData(event.target)
        })
            .then(response => response.json())
            .then(data => {
                // Notificar correcto POST
                console.log(data.message);
                formulario.reset();

                // TODO success banner
            })
            .catch((error) => {
                // Notificar POST erróneo
                console.error('Error:', error);
            });
    }
);
