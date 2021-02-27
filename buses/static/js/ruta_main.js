// Inicio de las apps de rutas
// Cargamos el template en la sección de hora para que sea usado por Vue3
document.getElementById("DigitalCLOCK").innerText = "{{ hora }}";

// // Main Vue app
const ruta_app = Vue.createApp({
    data () {
        return {
            hello: "world",
            hora: "-",
            tiempo_en_minutos: 0, // Con este elemento se recorren los arreglos de horarios
            desde_sanjose: [], //WARN: debe estar declarado anteriormente en el document
            hacia_sanjose: [],
        };
    },
    mounted () { // Estos metodos ejecutan en todo momento
        setInterval(() => { // Lógica de la aplicación HORADIGITAL
            var time = new Date();
            this.tiempo_en_minutos = time.getMinutes() + time.getHours()*60;
            this.hora = time.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true });
        }, 1000); // Cada segundo refresca
        setInterval(() => { // Lógica de proximobus

            // FIXME: Esta parte no me gusta
            var time = new Date();
            this.desde_sanjose = [];
            horario_desde_sanjose.filter(
                value => value[0] > this.tiempo_en_minutos ) // Mayores a la hora
                .slice(0,3) // Los siguientes 3
                .forEach(element => {
                    time.setHours(element[1]);
                    time.setMinutes(element[2]);
                    this.desde_sanjose.push(
                        [
                            time.toLocaleString(
                                'en-US', { hour: 'numeric', minute: 'numeric', hour12: true }),
                            element[3] // Ramal
                        ]);
                });
            this.hacia_sanjose = [];
            horario_hacia_sanjose.filter(
                value => value[0] > this.tiempo_en_minutos ) // Mayores a la hora
                .slice(0,3) // Los siguientes 3
                .forEach(element => {
                    time.setHours(element[1]);
                    time.setMinutes(element[2]);
                    this.hacia_sanjose.push(
                        [
                            time.toLocaleString(
                                'en-US', { hour: 'numeric', minute: 'numeric', hour12: true }),
                            element[3] // Ramal
                        ]);
                });
            // END FIXME
        }, 60000); // Cada 60 segundos refresca
    }
});

ruta_app.mount('#ruta_vue_app');

// TODO:
// Hora (listo)
// Próximo bus (casi)
// Mapa
