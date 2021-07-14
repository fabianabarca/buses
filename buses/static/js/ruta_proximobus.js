ruta_app.component('proximobus', {
    props: ['route_short_name'],
    template: `
<div class="container">
<div class="row">
<div class="col">
                {{ route_short_name }}
                <i class="fas fa-arrow-circle-right color-ruta"></i> San&nbsp;José
</div>
<div class="col">
                  San José <i class="fas fa-arrow-circle-right color-ruta"></i>
                  {{ route_short_name }}
</div>
</div>

<!-- Primera fila -->
<div class="row font-weight-bold">
    <div class="col" v-if="hacia_sanjose[0]" style="font-size: 1.25rem;">
        <span class="align-middle">{{ hacia_sanjose[0] }}</span>&nbsp;
        <span v-if="is_badge_visible(hacia_sanjose_ramal[0])"
            :class="['badge', 'custom-badge',
            filter_badge(hacia_sanjose_ramal[0])
            ]">{{ hacia_sanjose_ramal[0] }}</span>
    </div>
    <div class="col" v-else>No hay más buses hoy</div>

    <div class="col" v-if="desde_sanjose[0]" style="font-size: 1.25rem;">
        <span class="align-middle">{{ desde_sanjose[0] }}</span>&nbsp;
        <span v-if="is_badge_visible(desde_sanjose_ramal[0])"
            :class="['badge', 'custom-badge',
            filter_badge(desde_sanjose_ramal[0])
            ]">{{ desde_sanjose_ramal[0] }}</span>
    </div>
    <div class="col" v-else>No hay más buses hoy</div>
</div>

<!-- Segunda fila -->
<div class="row font-weight-bold">
<div class="col">
        <span v-if="hacia_sanjose[1]" class="align-middle">{{ hacia_sanjose[1] }}</span>&nbsp;
        <span v-if="is_badge_visible(hacia_sanjose_ramal[1])"
            :class="['badge', 'custom-badge',
            filter_badge(hacia_sanjose_ramal[1])
            ]">{{ hacia_sanjose_ramal[1] }}</span>
    </div>
    <div class="col">
        <span v-if="desde_sanjose[1]" class="align-middle">{{ desde_sanjose[1] }}</span>&nbsp;
        <span v-if="is_badge_visible(desde_sanjose_ramal[1])"
            :class="['badge', 'custom-badge',
            filter_badge(desde_sanjose_ramal[1])
            ]">{{ desde_sanjose_ramal[1] }}</span>
    </div>
</div>

<!-- Tercera fila -->
<div class="row font-weight-bold">
    <div class="col">
        <span v-if="hacia_sanjose[2]" class="align-middle">{{ hacia_sanjose[2] }}</span>&nbsp;
        <span v-if="is_badge_visible(hacia_sanjose_ramal[2])"
            :class="['badge', 'custom-badge',
            filter_badge(hacia_sanjose_ramal[2])
            ]">{{ hacia_sanjose_ramal[2] }}</span>
    </div>
    <div class="col">
        <span v-if="desde_sanjose[2]" class="align-middle">{{ desde_sanjose[2] }}</span>&nbsp;
        <span v-if="is_badge_visible(desde_sanjose_ramal[2])"
            :class="['badge', 'custom-badge',
            filter_badge(desde_sanjose_ramal[2])
            ]">{{ desde_sanjose_ramal[2] }}</span>
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
            if (ramal == 'SG') return 'invisible';
            if (ramal == 'AC') return 'badge-secondary';
            if (ramal == 'SL') return 'fondo-color-sanluis';
            if (ramal == 'TU') return 'fondo-color-turrujal';
            if (ramal == 'JO') return 'badge-secondary';
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
