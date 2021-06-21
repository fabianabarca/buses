ruta_app.component('proximobus', {
    props: ['route_short_name'],
    template: `
        <table class="table table-borderless">
          <thead class="table-light">
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

<!-- Primer fila -->
<tr>
    <td v-if="hacia_sanjose[0]" class="font-weight-bold">
        <span class="align-middle">{{ hacia_sanjose[0] }}</span>&nbsp;
        <span :class="['badge', 'custom-badge',
            hacia_sanjose_ramal[0] == 'AC' ? 'badge-secondary':'',
            hacia_sanjose_ramal[0] == 'SL' ? 'badge-danger':'',
            hacia_sanjose_ramal[0] == 'TU' ? 'badge-warning':'',
            hacia_sanjose_ramal[0] == 'JO' ? 'badge-info':'',
            ]">{{ hacia_sanjose_ramal[0] }}</span>
    </td>
    <td v-else class="font-weight-bold">No hay más buses hoy</td>

    <td v-if="desde_sanjose[0]" class="font-weight-bold">
        <span class="align-middle">{{ desde_sanjose[0] }}</span>&nbsp;
        <span :class="['badge', 'custom-badge',
            desde_sanjose_ramal[0] == 'AC' ? 'badge-secondary':'',
            desde_sanjose_ramal[0] == 'SL' ? 'badge-danger':'',
            desde_sanjose_ramal[0] == 'TU' ? 'badge-warning':'',
            desde_sanjose_ramal[0] == 'JO' ? 'badge-info':'',
            ]">{{ desde_sanjose_ramal[0] }}</span>
    </td>
    <td v-else class="font-weight-bold">No hay más buses hoy</td>
</tr>

<!-- Segunda fila -->
<tr>
    <td class="font-weight-bold">
        <span v-if="hacia_sanjose[1]" class="align-middle">{{ hacia_sanjose[1] }}</span>&nbsp;
        <span v-if="hacia_sanjose[1]" :class="['badge', 'custom-badge',
            hacia_sanjose_ramal[1] == 'AC' ? 'badge-secondary':'',
            hacia_sanjose_ramal[1] == 'SL' ? 'badge-danger':'',
            hacia_sanjose_ramal[1] == 'TU' ? 'badge-warning':'',
            hacia_sanjose_ramal[1] == 'JO' ? 'badge-info':'',
            ]">{{ desde_sanjose_ramal[1] }}</span>
    </td>

    <td class="font-weight-bold">
        <span v-if="desde_sanjose[1]" class="align-middle">{{ desde_sanjose[1] }}</span>&nbsp;
        <span v-if="desde_sanjose[1]" :class="['badge', 'custom-badge',
            desde_sanjose_ramal[1] == 'AC' ? 'badge-secondary':'',
            desde_sanjose_ramal[1] == 'SL' ? 'badge-danger':'',
            desde_sanjose_ramal[1] == 'TU' ? 'badge-warning':'',
            desde_sanjose_ramal[1] == 'JO' ? 'badge-info':'',
            ]">{{ desde_sanjose_ramal[1] }}</span>
    </td>
</tr>

<!-- Tercer fila -->
<tr>
    <td class="font-weight-bold">
        <span v-if="hacia_sanjose[2]" class="align-middle">{{ hacia_sanjose[2] }}</span>&nbsp;
        <span v-if="hacia_sanjose[2]" :class="['badge', 'custom-badge',
            hacia_sanjose_ramal[2] == 'AC' ? 'badge-secondary':'',
            hacia_sanjose_ramal[2] == 'SL' ? 'badge-danger':'',
            hacia_sanjose_ramal[2] == 'TU' ? 'badge-warning':'',
            hacia_sanjose_ramal[2] == 'JO' ? 'badge-info':'',
            ]">{{ desde_sanjose_ramal[2] }}</span>
    </td>

    <td class="font-weight-bold">
        <span v-if="desde_sanjose[2]" class="align-middle">{{ desde_sanjose[2] }}</span>&nbsp;
        <span v-if="desde_sanjose[2]" :class="['badge', 'custom-badge',
            desde_sanjose_ramal[2] == 'AC' ? 'badge-secondary':'',
            desde_sanjose_ramal[2] == 'SL' ? 'badge-danger':'',
            desde_sanjose_ramal[2] == 'TU' ? 'badge-warning':'',
            desde_sanjose_ramal[2] == 'JO' ? 'badge-info':'',
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
