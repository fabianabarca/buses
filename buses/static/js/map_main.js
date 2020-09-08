/* 
    MAPAS DE Leaflet JS BASADOS EN OpenStreetMap


    POR AHORA SOLO ESTÁN LOS PUNTOS REFERENTES 
    A LA PARADA EN SJ Y A LA PARADA EN SAN GABRIEL
    
    UNA VEZ SE TENGAN TODAS LAS PARADAS EN EL OBJETO 
    "STOP" DEL MODELO DE RUTAS, SE PUEDEN INGRESAR
    TODOS ESOS PUNTOS Y CREAR LA RUTA
*/

let osmUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    osmAttrib = '&copy; <a href="http://openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    osm = L.tileLayer(osmUrl, {maxZoom: 18, attribution: osmAttrib});
let map = L.map('map').setView([0, 0], 15).addLayer(osm);

L.marker([9.787471, -84.106066])
    .addTo(map)
    .bindPopup('Terminal San Gabriel de Acosta')
    .openPopup();
L.marker([9.928808, -84.076289])
    .addTo(map)
    .bindPopup('Parada en San José para San Gabriel de Acosta')
    .openPopup();

map.setZoom(11);