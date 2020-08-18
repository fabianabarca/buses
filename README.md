# web-buses: estructura de la página web

Todas las páginas tienen dentro de *base.html*:

- Encabezado: logo, íconos de las rutas, menú plegado
- Pie: menú completo, otra información

## Arquitectura de información (inventario de contenidos)

- **/** : (*index.html*) : avisos, próximos buses, noticias, (publicidad)
    - **/rutas/** : (*rutas.html*) : lista de rutas de la empresa
        - **/rutas/sangabriel/** : (*ruta.html*) : próximo bus, horario, precios, mapas, (publicidad)
        - **/rutas/acosta/** : (*ruta.html*) : próximo bus, horario, precios, mapas, (publicidad)
        - **/rutas/…** : (*ruta.html*) : otras rutas
    - **/noticias/** : (*noticias.html*) : avisos, noticias (registro histórico de noticias)
    - **/nosotros/** : (*empresa.html*) : reseña de la empresa, socios, patrocinadores
        - **/nosotros/personal/** : (*personal.html*) : personal, cumpleaños
    - **/comunidades/** : (*comunidades.html*) : reseña de la zona
        - **/comunidades/sangabriel/** : (*comunidad.html*) : historia de San Gabriel
        - **/comunidades/acosta/** : (*comunidad.html*) : historia de Acosta
        - **/comunidades/…** : (*comunidad.html*) : historia de otras comunidades
    - **/contacto/** : (*contacto.html*) : correo y teléfono, formulario de contacto (varios opciones: objetos perdidos, para mejorar, denuncias, etc.)

## Apps

- Inicio (Fabián)
- Rutas (Anyelo)
- Empresa (Fabián)
- Noticias (David)
- Información (Fabián)

## Modelos para cada app

- **Noticias** —> informaciones temporales para desplegar en varias secciones
    - (`class`) **Noticia**: noticias generales que se muestran en inicio y en sección noticias
        - título
        - fecha
        - descripción corta
        - descripción larga
        - documento (opcional)
        - expiración
    - (`class`) **Aviso**: avisos urgentes que se muestran en contenedor especial en página de inicio y en la de noticias
        - título
        - fecha
        - descripción corta
        - expiración
        - urgencia (1, 2, 3, asociado con íconos)
        - ligar a una noticia (opcional, crear noticia, ahí agregar documento)

- **Información** —> páginas estáticas con información que generalmente no va a cambiar
    - (`class`) **Contenido**: información genérica (para reseñas, comunidades, contacto)
        - título
        - contenido
        - …
    - (`class`) **Comunidad**: información de las comunidades
        - nombre
        - url
        - historia
        - foto
        - …

- **Empresa** —> información y actores relacionados con la empresa
    - (`class`) **Empresa**: información general de la empresa
        - descripción
    - (`class`) **Personal**: descripción de todos los colaboradores
        - nombre
        - apellido
        - puesto
        - foto
        - …
    - (`class`) **Socio**: descripción de todos los socios
        - …
    - (`class`) **Patrocinador**: descripción de todos los patrocinadores
        - …

- **Rutas** —> información del servicio según GTFS
    - (`class`) **Agencia**: (agency) información general de la empresa, según GTFS
        - agency_id
        - agency_name
        - agency_url
        - …
    - (`class`) **Parada**: (stops) información de las paradas autorizadas, según GTFS
        - stop_id
        - stop_code
        - stop_name
        - …
    - (`class`) **Ruta**: (routes) información general de la ruta, según GTFS
        - route_id
        - agency_id
        - route_short_name
        - …
    - (`class`) **Viaje**: (trips) cada uno de los viajes con su horario, según GTFS
        - route_id
        - service_id
        - trip_id
        - …
    - (`class`) **Horario**: (stop_times) la hora de partida de cada viaje
        - trip_id
        - arrival_time
        - departure_time
        - …
    - (`class`) **Calendario**: (calendar) días en que funciona con distintos horarios (entre semana, sábados, domingos)
        - service_id (“entre_semana”, “sabado”, “domingo”, “feriado”)
        - monday
        - tuesday
        - … (ejemplo: entre_semana,1,1,1,1,1,0,0,20200815,20200915)
    - (`class`) **Feriado**: (calendar_dates) excepciones a Calendario para los feriados del año
        - service_id
        - date
        - exception_type

## *Templates* para cada app

- **Rutas**
    - *index.html*: página principal del sitio
    - *rutas.html*: lista de rutas
        - *ruta.html*: descripción de cada ruta

- **Noticias**
    - *noticias.html*: lista de noticias
    
- **Empresa**
    - *empresa.html*: reseña de la empresa
        - *personal.html*: lista de personal

- **Información**
    - *comunidades.html*: reseña y lista de comunidades
        - *comunidad.html*: descripción de cada comunidad
    - *contacto.html*: información y formulario de contacto

## Notas mentales

- Es posible importar modelos desde otras apps. Por ejemplo, para agregar un aviso en otra app, se puede hacer en `models.py` de rutas: `from noticias.modelos import Aviso` y utilizarlo ahí y dentro de `views.py`.
- En `views.py` se “inyectan” las variables de interés a la página que se quiere mostrar mediante el *context* (un diccionario) que se referencia como `{{ variable }}` o `{{ variable.atributo }}` dentro del *template*. Por tanto, operaciones especiales se crean en `views.py`.
- Hay una relación casi 1:1:1 entre `urls` -> `views` -> `templates`. Una `url` para cada `view` que tiene un `template`, donde se utilizan variables que vienen de los `models`.
