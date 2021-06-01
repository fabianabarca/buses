 /*
  * La siguiente función de JavaScript coloca la hora segundo a segundo en el
  * elemento cuyo ID sea enviado como parámetro a la misma
  * Este código se escribe como soporte a algunas peticiones de código que
  * dependían de la rutina anterior
  * Se recomienta sustituir todas estas llamadas in-place por alguna implementación
  * interna en la app Vue de cada página.
  */

function displayTimeOn (elementID) {
    var l_element = document.getElementById(elementID);
    if ( l_element ){
        function addZero(i) {
            if (i < 10) {
                i = "0" + i;
            }
            return i;
        }
        window.setInterval(function () {
            var l_date = new Date();
            var h = addZero(l_date.getHours());
            var m = addZero(l_date.getMinutes());
            var s = addZero(l_date.getSeconds());
            l_element.innerText = h + ":" + m + ":" + s;
        }, 1000);
    } else throw Error ("Element with ID: "+l_element+" does not exist");
}
