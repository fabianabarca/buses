// Inicioooo de las apps de rutas

// // Main Vue app
const ruta_app = Vue.createApp({
    data () {
        return {
            hora: "--:-- --",
            day: dayjs().day(), // 0 dom; 1-5 lun,mar,mie,jue,vie; 6 sab

            // Download tables as images:
            table_on_select: 'entresemana_table',
        };
    },
    methods: {
        downloadTableAsImage() {
            var my_table_id = this.table_on_select; // FIXME

            html2canvas(document.getElementById(my_table_id)).then(
                canvas => {

                    var a = document.createElement("a");
                    a.download = 'horario_'+this.table_on_select+'.jpeg';
                    a.href = canvas.toDataURL("image/jpeg");
                    a.dataset.downloadurl = ["image/jpeg", a.download, a.href].join(":");
                    a.style.display = "none";
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    setTimeout(function () {
                        URL.revokeObjectURL(a.href);
                    }, 1500);
                });
        },
        showHideStopInfo(stop_id, event){

            // Definir si se hizo click sobre la flecha o el contenedor circular
            let target = event.target;
            if (event.target.childElementCount) target = event.target.childNodes[0];

            // Cambiar la dirección de la flecha
            if ( target.classList.contains('fa-arrow-down')){
                target.classList.add("fa-arrow-right");
                target.classList.remove("fa-arrow-down");
            } else {
                target.classList.add("fa-arrow-down");
                target.classList.remove("fa-arrow-right");
            }

            // Mostrar u ocultar la ficha informativa según el caso
            if (document.getElementById('short_name_stop_id_'+stop_id).hidden){
                document.getElementById('short_name_stop_id_'+stop_id).hidden = false;
                document.getElementById('info_stop_id_'+stop_id).hidden = true;
            }else {
                document.getElementById('short_name_stop_id_'+stop_id).hidden = true;
                document.getElementById('info_stop_id_'+stop_id).hidden = false;
            }
        },
    },
    mounted () {
        setInterval(() => { // Lógica de la aplicación HORADIGITAL
            var time = dayjs();
            this.tiempo_en_minutos = time.minute() + time.hour()*60;
            this.hora = time.format('h:mm:ss A');
        }, 1000); // Cada segundo refresca

        // El horario activo según el día de la semana
        if (!dayjs().day())
            this.table_on_select = "domingo_table" ;
        else if (dayjs().day() == 6)
            this.table_on_select = "sabado_table" ;
        else
            this.table_on_select = "entresemana_table" ;
    },
});
