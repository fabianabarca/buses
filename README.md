# web-buses: estructura de la página web

Cómo comenzar a programar:
[Developer setup](./dev_setup.md)
(Comparte cualquier duda para mejorar la documentación)

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

- Inicio
- Rutas
- Empresa
- Noticias
- Comunidades
- Contacto

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

- **Comunidades** —> páginas estáticas con reseñas de la comunidad que generalmente no va a cambiar
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

- **Contacto** —> página de contacto con la empresa
    - (`class`) **Formulario**: formulario de contacto
        - nombre
        - correo
        - asunto
        - texto
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

- **Inicio**
    - *index.html*: página principal del sitio

- **Rutas**
    - *rutas.html*: lista de rutas
        - *ruta.html*: descripción de cada ruta

- **Noticias**
    - *noticias.html*: lista de noticias
    
- **Empresa**
    - *empresa.html*: reseña de la empresa
        - *personal.html*: lista de personal

- **Comunidades**
    - *comunidades.html*: reseña y lista de comunidades
        - *comunidad.html*: descripción de cada comunidad

- **Contacto**
    - *contacto.html*: información y formulario de contacto

## Recursos

Normas técnicas de accesibilidad: https://drive.google.com/drive/folders/1wUJ9ADHaZNMxUSJ3Sl0tc5g-T8ArNah8

## Notas mentales

- Es posible importar modelos desde otras apps. Por ejemplo, para agregar un aviso en otra app, se puede hacer en `models.py` de rutas: `from noticias.modelos import Aviso` y utilizarlo ahí y dentro de `views.py`.
- En `views.py` se “inyectan” las variables de interés a la página que se quiere mostrar mediante el *context* (un diccionario) que se referencia como `{{ variable }}` o `{{ variable.atributo }}` dentro del *template*. Por tanto, operaciones especiales se crean en `views.py`.
- Hay una relación casi 1:1:1 entre `urls` -> `views` -> `templates`. Una `url` para cada `view` que tiene un `template`, donde se utilizan variables que vienen de los `models`.

## Tareas próximas

- [ ] Migración o generación de contenidos - *Juan Manuel Chavarría, Luis Jiménez*
- [ ] Creación del estilo CSS de un `<div>` contenedor de las rutas - *María Paula*
- [ ] Selección de colores por ruta - *María Paula*
- [ ] Búsqueda de nueva plantilla con: menú superior fijo, cuadrícula para personal, banner para noticias, cuadros de avisos (ojalá que no sea Bootstrap) - *Peter, Caly*
- [ ] Revisión de las recomendaciones WCAG 2.1 - *Stacy*
- [ ] Preparación del hospedaje en AWS - *Luis Carlos, Santiago, Luis Guillermo, Marisol*
- [ ] Nuevo logo - *José Pablo Laurent, Luis Jiménez, María Laura*
- [ ] Edición enriquecida de texto para `models.TextField()` - *Marisol*
- [ ] Contenido de comunidades (San Gabriel, Acosta, Vuelta de Jorco, Tarbaca) - *José Pablo Laurent, Luis Jiménez, Juan Manuel Chavarría*
- [ ] Formulario de contacto con correo electrónico (incluye determinación de tipos de dudas) - *Jeancarlo*
- [ ] Aplicación "próximo bus" - *Anyelo*
- [ ] GTFS "alternativo" (primera versión) - *Anyelo*
- [ ] Trabajar en los templates de los apps - *Fabián*
- [ ] Noticias y avisos - *David Retana*
- [ ] ...
