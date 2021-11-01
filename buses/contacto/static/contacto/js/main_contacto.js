// Contact form page JS

// Se hace query del formulario
const formulario = document.querySelector('form');
const form_alerts = formulario.getElementsByClassName("form_alerts")[0]; // .childNodes[1];

// TODO agregar listener a cada input para validar los datos por aparte con JS

let validarInputTelefono = element => {
    if ( ! element.value.length ){
        element.classList.remove("is-valid");
        element.classList.remove("is-invalid");
    } else if ( // Si no tiene un + el número se observa si es un entero
        (element.value.split("+").length == 1) &&
            ( Number.isInteger(Number(element.value.replace(/[- ]/g, ""))) )
    ){
        element.classList.remove("is-invalid");
        element.classList.add("is-valid");
    } else if ( // Si tiene un + se toma unicamente el número se observa si es un entero
        (element.value.split("+").length == 2) &&
            ( Number.isInteger(Number(element.value.split("+")[1].replace(/[- ]/g, ""))) )
    ){
        element.classList.remove("is-invalid");
        element.classList.add("is-valid");
    } else { // Si no es un número entero entonces es inválido
        element.classList.remove("is-valid");
        element.classList.add("is-invalid");
    }
};

let validarInputCorreo = element => {
    if ( ! element.value.length ){
        element.classList.remove("is-valid");
        element.classList.remove("is-invalid");
    } else if ( // Si el correo tiene un @
        (element.value.split("@").length == 2) &&
        (element.value.split("@")[1].split(".").length == 2)
    ){
        element.classList.remove("is-invalid");
        element.classList.add("is-valid");
    } else { // Si el correo no tiene @
        element.classList.remove("is-valid");
        element.classList.add("is-invalid");
    }
};

let formularioValidarDato = event => {
    // Al introducir cosas en el Form se ocultan las alertas del formulario
    form_alerts.classList.add("form_alerts_hide");
    form_alerts.querySelector("DIV").classList.remove("alert-success");

    switch (event.target.name) { // Validación dependiendo el input
    case "telefono":
        validarInputTelefono(event.target);
        break;
    case "nombre":
        // Verificar un tamaño mínimo
        if ( ! event.target.value.length ){
            event.target.classList.remove("is-valid");
            event.target.classList.remove("is-invalid");
        } else if ( event.target.value.length < 2 ){
            event.target.classList.add("is-invalid");
            event.target.classList.remove("is-valid");
        } else {
            event.target.classList.add("is-valid");
            event.target.classList.remove("is-invalid");
        }
        break;
    case "email":
        validarInputCorreo(event.target);
        break;
    case "mensaje":
        // Verificar que no exceda los 500 characters
        if ( ! event.target.value.length ){
            event.target.classList.remove("is-valid");
            event.target.classList.remove("is-invalid");
        } else if ( event.target.value.length > 500 ){
            event.target.classList.add("is-invalid");
            event.target.classList.remove("is-valid");
        } else {
            event.target.classList.add("is-valid");
            event.target.classList.remove("is-invalid");
        }
        break;
    default:
        // No se hace nada
        break;
    }
};


formulario.addEventListener(
    'input',
    formularioValidarDato
);

formulario.addEventListener(
    'submit',
    event => {
        // Se cancela el refresh
        event.preventDefault();

        // Hacemos el post a través de fetch
        if (
            (form_alerts.querySelector("DIV").classList.contains("alert-success")) ||
            (formulario.querySelectorAll(".is-invalid").length) // Si hay inputs inválidos
        ){
            // Ya fue enviado el formulario o hay inputs inválidos, no hacer nada
        } else {
            // Enviar el formulario por primera vez
            fetch("post_form", {
            method: "POST",
            body: new FormData(event.target)
        })
            .then(response => response.json())
            .then(data => {
                // Notificar correcto POST
                console.log(data.message);

                // Success banner
                form_alerts.classList.remove("form_alerts_hide");
                form_alerts.querySelector("DIV").classList.remove("alert-danger");
                form_alerts.querySelector("DIV").classList.add("alert-success");
                form_alerts.querySelector("DIV").innerHTML='<i class="fas fa-info-circle"></i> Formulario <strong>enviado</strong> correctamente! Gracias!';

                // TODO presentar cuando hay errores del lado del servidor (5xx)
            })
            .catch((error) => {
                // Notificar POST erróneo
                console.error('Error:', error);
                form_alerts.classList.remove("form_alerts_hide");
                form_alerts.querySelector("DIV").classList.remove("alert-success");
                form_alerts.querySelector("DIV").classList.add("alert-danger");
                form_alerts.querySelector("DIV").innerHTML="Formulario <strong>no enviado</strong> debido a error de conectividad.";
            });
        }
    }
);

formulario.addEventListener(
    'reset',
    event => {
        // Al ejecutar un reset se ocultan las alertas del formulario
        formulario.querySelectorAll(".is-valid").forEach(element => element.classList.remove("is-valid"));
        formulario.querySelectorAll(".is-invalid").forEach(element => element.classList.remove("is-invalid"));

        form_alerts.classList.add("form_alerts_hide");
        form_alerts.querySelector("DIV").classList.remove("alert-success");
    }
);
