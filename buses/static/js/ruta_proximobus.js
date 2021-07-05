ruta_app.component('proximobus', {
    props: ['route_short_name'],
    template: `
        <table class="table table-borderless">
          <thead class="table-secondary">
            <tr>
              <th>
                {{ route_short_name }}
                <i class="fas fa-arrow-circle-right"></i> San&nbsp;José
              </th>
              <th>
                  San José <i class="fas fa-arrow-circle-right"></i>
                  {{ route_short_name }}
              </th>
            </tr>
          </thead>

<tbody>

<!-- Primera fila -->
<tr>
    <td v-if="hacia_sanjose[0]" class="font-weight-bold lead">
        <span class="align-middle">{{ hacia_sanjose[0] }}</span>&nbsp;
        <span v-if="is_badge_visible(hacia_sanjose_ramal[0])"
            :class="['badge', 'custom-badge',
            filter_badge(hacia_sanjose_ramal[0])
            ]">{{ hacia_sanjose_ramal[0] }}</span>
    </td>
    <td v-else class="font-weight-bold">No hay más buses hoy</td>

    <td v-if="desde_sanjose[0]" class="font-weight-bold lead">
        <span class="align-middle">{{ desde_sanjose[0] }}</span>&nbsp;
        <span v-if="is_badge_visible(desde_sanjose_ramal[0])"
            :class="['badge', 'custom-badge',
            filter_badge(desde_sanjose_ramal[0])
            ]">{{ desde_sanjose_ramal[0] }}</span>
    </td>
    <td v-else class="font-weight-bold">No hay más buses hoy</td>
</tr>

<!-- Segunda fila -->
<tr>
    <td class="font-weight-bold">
        <span v-if="hacia_sanjose[1]" class="align-middle">{{ hacia_sanjose[1] }}</span>&nbsp;
        <span v-if="is_badge_visible(hacia_sanjose_ramal[1])"
            :class="['badge', 'custom-badge',
            filter_badge(hacia_sanjose_ramal[1])
            ]">{{ hacia_sanjose_ramal[1] }}</span>
    </td>

    <td class="font-weight-bold">
        <span v-if="desde_sanjose[1]" class="align-middle">{{ desde_sanjose[1] }}</span>&nbsp;
        <span v-if="is_badge_visible(desde_sanjose_ramal[1])"
            :class="['badge', 'custom-badge',
            filter_badge(desde_sanjose_ramal[1])
            ]">{{ desde_sanjose_ramal[1] }}</span>
    </td>
</tr>

<!-- Tercer fila -->
<tr>
    <td class="font-weight-bold">
        <span v-if="hacia_sanjose[2]" class="align-middle">{{ hacia_sanjose[2] }}</span>&nbsp;
        <span v-if="is_badge_visible(hacia_sanjose_ramal[2])"
            :class="['badge', 'custom-badge',
            filter_badge(hacia_sanjose_ramal[2])
            ]">{{ hacia_sanjose_ramal[2] }}</span>
    </td>

    <td class="font-weight-bold">
        <span v-if="desde_sanjose[2]" class="align-middle">{{ desde_sanjose[2] }}</span>&nbsp;
        <span v-if="is_badge_visible(desde_sanjose_ramal[2])"
            :class="['badge', 'custom-badge',
            filter_badge(desde_sanjose_ramal[2])
            ]">{{ desde_sanjose_ramal[2] }}</span>
    </td>
</tr>

</tbody>
</table>
`,
    data: function () {
        return {
            tiempo_en_minutos: 0, // Con este elemento se recorren los arreglos de horarios

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
            horario_desde_sanjose.filter(
                value => value[0] > this.tiempo_en_minutos ) // Mayores a la hora
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
                value => value[0] > this.tiempo_en_minutos ) // Mayores a la hora
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
