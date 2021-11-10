// Contact form page JS, type="module", private scope, vanilla JS

////////////////////////////////////////////////////////////////
////////////////// Elementos del formulario a utilizar /////////
////////////////////////////////////////////////////////////////

// Se hace query del formulario
let formulario = document.querySelector("form");
let form_alerts = formulario.getElementsByClassName("form_alerts")[0]; // .childNodes[1];
let form_nombre = document.getElementById("id_nombre");
let form_telefono = document.getElementById("id_telefono");
let form_mensaje = document.getElementById("id_mensaje");
let form_email = document.getElementById("id_email");

////////////////////////////////////////////////////////////////
////////////////// Definir los métodos para cada evento ////////
////////////////////////////////////////////////////////////////

let validarInputNombre = (event) => {
  // Verificar un tamaño mínimo
  if (!event.target.value.length) {
    event.target.classList.remove("is-valid");
    event.target.classList.remove("is-invalid");
  } else if (event.target.value.length < 2) {
    event.target.classList.add("is-invalid");
    event.target.classList.remove("is-valid");
  } else {
    event.target.classList.add("is-valid");
    event.target.classList.remove("is-invalid");
  }
};

let validarInputTelefono = (event) => {
  let element = event.target;
  if (!element.value.length) {
    element.classList.remove("is-valid");
    element.classList.remove("is-invalid");
  } else if (
    // Si no tiene un + el número se observa si es un entero
    element.value.split("+").length == 1 &&
    Number.isInteger(Number(element.value.replace(/[- ]/g, "")))
  ) {
    element.classList.remove("is-invalid");
    element.classList.add("is-valid");
  } else if (
    // Si tiene un + se toma unicamente el número se observa si es un entero
    element.value.split("+").length == 2 &&
    Number.isInteger(Number(element.value.split("+")[1].replace(/[- ]/g, "")))
  ) {
    element.classList.remove("is-invalid");
    element.classList.add("is-valid");
  } else {
    // Si no es un número entero entonces es inválido
    element.classList.remove("is-valid");
    element.classList.add("is-invalid");
  }
};

let validarInputCorreo = (event) => {
  let element = event.target;
  if (!element.value.length) {
    element.classList.remove("is-valid");
    element.classList.remove("is-invalid");
  } else if (
    // Si el correo tiene un @
    element.value.split("@").length == 2 &&
    element.value.split("@")[1].split(".").length > 2
  ) {
    element.classList.remove("is-invalid");
    element.classList.add("is-valid");
  } else {
    // Si el correo no tiene @
    element.classList.remove("is-valid");
    element.classList.add("is-invalid");
  }
};

let validarInputMensaje = (event) => {
  // Verificar que no exceda los 500 characters
  if (!event.target.value.length) {
    event.target.classList.remove("is-valid");
    event.target.classList.remove("is-invalid");
  } else if (event.target.value.length > 500) {
    event.target.classList.add("is-invalid");
    event.target.classList.remove("is-valid");
  } else {
    event.target.classList.add("is-valid");
    event.target.classList.remove("is-invalid");
  }
};

let formularioOnInput = (event) => {
  // Al introducir cosas en el Form se ocultan las alertas del formulario
  form_alerts.classList.add("form_alerts_hide");
  form_alerts.querySelector("DIV").classList.remove("alert-success");
};

let formularioOnSubmit = (event) => {
  // Se cancela el refresh
  event.preventDefault();

  // Validar que todos los espacios están completos:
  if (!form_nombre.value.length) form_nombre.classList.add("is-invalid");

  // Validar el contenido del input de teléfono
  validarInputTelefono({ target: form_telefono });
  // if (! form_telefono.value.length ) // Opcional
  //     form_telefono.classList.add("is-invalid");

  // Validar el correo y invalidar si está vacío
  validarInputCorreo({ target: form_email });
  if (!form_email.value.length) form_email.classList.add("is-invalid");

  if (!form_mensaje.value.length) form_mensaje.classList.add("is-invalid");

  // Hacemos el post a través de fetch
  if (
    form_alerts.querySelector("DIV").classList.contains("alert-success") ||
    formulario.querySelectorAll(".is-invalid").length // Si hay inputs inválidos
  ) {
    // Ya fue enviado el formulario o hay inputs inválidos, no hacer nada
  }
  // Enviar el formulario por primera vez
  else
    (async () => {
      try {
        let response = await fetch("post_form", {
          method: "POST",
          body: new FormData(event.target),
        });
        let data = await response.json();

        // Notificar correcto POST
        if (response.ok) {
          // Success banner
          form_alerts.classList.remove("form_alerts_hide");
          form_alerts.querySelector("DIV").classList.remove("alert-danger");
          form_alerts.querySelector("DIV").classList.add("alert-success");
          form_alerts.querySelector("DIV").innerHTML = data.message;
        } else {
          // Notificar POST erróneo server-side
          form_alerts.classList.remove("form_alerts_hide");
          form_alerts.querySelector("DIV").classList.remove("alert-success");
          form_alerts.querySelector("DIV").classList.add("alert-danger");
          form_alerts.querySelector("DIV").innerHTML = data.message;
        }
      } catch (error) {
        // Notificar POST erróneo por conectividad
        console.error("Error: ", error);
        form_alerts.classList.remove("form_alerts_hide");
        form_alerts.querySelector("DIV").classList.remove("alert-success");
        form_alerts.querySelector("DIV").classList.add("alert-danger");
        form_alerts.querySelector("DIV").innerHTML =
          "Formulario <strong>no enviado</strong> debido a error de conectividad.";
      }
    })();
};

let formularioOnReset = (event) => {
  // Al ejecutar un reset se ocultan las alertas del formulario
  formulario
    .querySelectorAll(".is-valid")
    .forEach((element) => element.classList.remove("is-valid"));
  formulario
    .querySelectorAll(".is-invalid")
    .forEach((element) => element.classList.remove("is-invalid"));

  form_alerts.classList.add("form_alerts_hide");
  form_alerts.querySelector("DIV").classList.remove("alert-success");
};

////////////////////////////////////////////////////////////
////////////////////////// Agregar los listener ////////////
////////////////////////////////////////////////////////////

form_nombre.addEventListener("input", validarInputNombre);

form_telefono.addEventListener("input", validarInputTelefono);

form_email.addEventListener("input", validarInputCorreo);

form_mensaje.addEventListener("input", validarInputMensaje);

formulario.addEventListener("input", formularioOnInput);

formulario.addEventListener("submit", formularioOnSubmit);

formulario.addEventListener("reset", formularioOnReset);
