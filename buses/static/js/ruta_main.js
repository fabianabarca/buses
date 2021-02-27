// Inicio de las apps de rutas
// Cargamos el template en la sección de hora para que sea usado por Vue3
document.getElementById("DigitalCLOCK").innerText = "{{ hora }}";

// Cargamos la App Vue, estática en el server, dinámica en frontend
fetch('/static/ruta_vue_app_proximobus.html').then(
    response => {
        switch (response.status) {
        case 200: // OK
            response.text().then( data =>{
                // document.getElementById(
                //     "proximo_bus_app").innerHTML = data;
                console.log("TODO: sustituir el innerHTML con el del template");
            });
            break;
        case 404: // Not found
            console.log('Not Found');
            break;
        }
    }
);

// // Funciones utilitarias
function proximos_buses () {
    console.log("proximo_bus_list");
}

// // Main Vue app
const app = Vue.createApp({
    data () {
        return {
            hello: "world",
            hora: 0,
        };
    },
    mounted () { // Estos metodos ejecutan en todo momento
        setInterval(() => {
            var time = new Date();
            this.hora = time.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true });
        }, 1000); // Cada segundo refresca
    }
});
app.mount('#ruta_vue_app');

// Hora
// Próximo bus
// Mapa
