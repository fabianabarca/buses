ruta_app.component('proximobus', {
    props: ['route_short_name'],
    template: `
<div class="container proxbus-container">

<div class="row proxbus-row proxbus-emph-row">
<div class="col">
                {{ route_short_name }} <i class="fas fa-arrow-circle-right color-ruta"></i> San&nbsp;José
</div>
<div class="col">
                  San José <i class="fas fa-arrow-circle-right color-ruta"></i> {{ route_short_name }}
</div>
</div>

<!-- Primera fila -->
<div class="row proxbus-row font-weight-bold">
    <div class="col proxbus-emph-col prox_izquierda" v-if="hacia_sanjose[0]">
      <div v-show="hacia_sanjose[0]" :class="[filter_badge(hacia_sanjose_ramal[0])]">{{ hacia_sanjose[0] }}</div>
    </div>
    <div class="col prox_izquierda" v-else>No hay más buses hoy</div>

    <div class="col proxbus-emph-col prox_derecha" v-if="desde_sanjose[0]">
      <div v-show="desde_sanjose[0]" :class="[filter_badge(desde_sanjose_ramal[0])]">{{ desde_sanjose[0] }}</div>
    </div>
    <div class="col prox_derecha" v-else>No hay más buses hoy</div>
</div>

<!-- Segunda fila -->
<div v-show="hacia_sanjose[1] || desde_sanjose[1]" class="row proxbus-row font-weight-bold">
  <div class='col prox_izquierda'>
    <div v-show="hacia_sanjose[1]" :class="[filter_badge(hacia_sanjose_ramal[1])]">{{ hacia_sanjose[1] }}</div>
  </div>
  <div class='col prox_derecha'>
    <div v-show="desde_sanjose[1]" :class="[filter_badge(desde_sanjose_ramal[1])]">{{ desde_sanjose[1] }}</div>
  </div>
</div>

<!-- Tercera fila -->
<div v-show="hacia_sanjose[2] || desde_sanjose[2]" class="row proxbus-row font-weight-bold">
  <div class='col prox_izquierda'>
    <div v-show="hacia_sanjose[2]" :class="[filter_badge(hacia_sanjose_ramal[2])]">{{ hacia_sanjose[2] }}</div>
  </div>
  <div class='col prox_derecha'>
    <div v-show="desde_sanjose[2]" :class="[filter_badge(desde_sanjose_ramal[2])]">{{ desde_sanjose[2] }}</div>
  </div>
</div>
</div>
`,
    data: function () {
        return {
            desde_sanjose: ['-','-','-'], // Horas
            hacia_sanjose: ['-','-','-'],

            desde_sanjose_ramal: [], // Ramales
            hacia_sanjose_ramal: [],
        };
    },
    methods: {
        is_badge_visible(ramal){
            // Si tiene length y no es SG
            if ( ramal && ( ramal != 'SG' ))  return true;
            return false;
        },
        filter_badge (ramal){
            if (ramal == 'SG') return 'time-badge-sangabriel';
            if (ramal == 'AC') return 'time-badge-acosta';
            if (ramal == 'SL') return 'time-badge-sanluis';
            if (ramal == 'TU') return 'time-badge-turrujal';
            if (ramal == 'JO') return 'time-badge-jorco';
            return '';
        },
        updateProximoBus: function(){
            // Lógica de proximobus
            this.desde_sanjose = [];
            var time = new Date();
            var time_to_minutes = time.getMinutes() + time.getHours()*60;
            horario_desde_sanjose.filter(
                value => value[0] > time_to_minutes ) // Mayores a la hora
                .slice(0,3) // Los siguientes 3
                .forEach((element, index) => {
                    time.setHours(element[1]);
                    time.setMinutes(element[2]);
                    this.desde_sanjose[index] = time.toLocaleString(
                        'en-US', { hour: 'numeric', minute: 'numeric', hour12: true });
                    this.desde_sanjose_ramal[index] = element[3]; // Ramal
                });

            this.hacia_sanjose = [];
            horario_hacia_sanjose.filter(
                value => value[0] > time_to_minutes ) // Mayores a la hora
                .slice(0,3) // Los siguientes 3
                .forEach((element, index) => {
                    time.setHours(element[1]);
                    time.setMinutes(element[2]);
                    this.hacia_sanjose[index] = time.toLocaleString(
                        'en-US', { hour: 'numeric', minute: 'numeric', hour12: true });
                    this.hacia_sanjose_ramal[index] = element[3]; // Ramal
                });
        },
    },
    mounted: function () {
        setInterval(() => {
            this.updateProximoBus();
        }, 1000); // Cada segundo refresca
    },
    created: function (){
        this.updateProximoBus();
    },
});
