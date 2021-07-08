 /*
  * La siguiente función de JavaScript coloca la hora segundo a segundo en el
  * elemento cuyo ID sea enviado como parámetro a la misma
  * Este código se escribe como soporte a algunas peticiones de código que
  * dependían de la rutina anterior
  * Se recomienta sustituir todas estas llamadas in-place por alguna implementación
  * interna en la app Vue de cada página.
  *
  * Depends: dayjs
  */

function displayTimeOn (elementID) {
    var l_element = document.getElementById(elementID);
    if ( l_element ){
        window.setInterval(function () {
            l_element.innerText = dayjs().format('h:mm:ss A');
        }, 1000);
    } else throw Error ("Element with ID: "+l_element+" does not exist");
}
