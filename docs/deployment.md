# Deployment - Actualización manual del proyecto en el servidor

El _deployment_ es el momento en el que colocamos nuestro código a disposición del equipo, e infraestructura del proyecto, en general se hace con la idea de evaluar la integración del software con los demás elementos a los cuales este debe servir, la mayor parte de la veces el deployment consiste en publicar de cierta forma el programa y ponerlo a funcionar como este normalmente lo haría en producción, en un servidor ya sea público o privado pero al cual las personas y servicios que nos interesan tengan acceso.

## Actualizar este proyecto utilizando la CLI

Lo primero que se debe hacer es entrar en una terminal con Bash o cualquier otro shell que sea POSIX.
Nos conectamos al servidor en el cual queremos montar el proyecto, para esto usamos ssh:

```bash
ssh -l tsg transportessangabriel.com
```

Detenemos el _service_ de _NGINX_ para realizar los cambios, **SOLO EN ESTE COMANDO DEL SISTEMA SE USA SUDO, NO UTILIZAR EN NINGÚN OTRO PASO**

```bash
sudo systemctl stop nginx.service
```

Ingresamos en el repositorio de interés, _produccion_ o _development_, y descargamos los cambios con el comando **git pull**

```bash
cd produccion
git pull
```

### Nuevas dependencias

En caso de que el proyecto tenga nuevas dependencias estas deberían estar escritas en el fichero _requirements.txt_ en el directorio del repositorio. Para instalar el nuevo software ejecutamos el comando:

```bash
pip install -r requirements.txt
```

### Usar estilos de aplicaciones de Django y de terceros

Tanto las aplicaciones de Django como las de terceros encapsulan su propio _/static/_ en el cual almacenan sus ficheros de JavaScript y CSS, estos se pueden ver correctamente cuando levantamos el servidor de desarrollo que viene con el framework, pero una vez que usamos el _WSGI_ en conjunto con _NGINX_ notaremos que las aplicaciones externas perderán sus estilos e interacciones de JavaScrip, esto sucede porque en producción no es sensato hacer peticiones de ficheros estáticos a través de un servición o rutina dinámica, por eso se espera que por parte del usuario se coloquen estos estilos y scripts en el directorio estático correspondiente al propio proyecto, este contenido será servido directamente por NGINX.

El comando _collectstatic_ de _manage.py_ recolecta todos los ficheros estáticos de las aplicaciones locales así como de aquellas que se encuentran en el ambiente virtual, e introducirá todos estos elementos en el directorio _staticfiles_ este es el directorio que debe ser servido por _NGINX_ ya que es autogenerado con cada actualización del proyecto. Para ejecutar la recolección de estáticos se ejecuta el siguiente comando estando en el virtual\_env y dentro del directorio que contiene el _manage.py_:

```bash
cd buses
./manage.py collectstatic
```

### Levantar el servicio 

Así como especificamos la IP permitida en el settings.py es necesario colocar el correcto **server\_name** en la configuración de Nginx, para esto editamos el fichero llamado _web-buses.nginx-config_ en el encontraremos dicha sección, ahí se colocará la URL del sitio o la IP en su defecto.

Antes de posicionar los ficheros de configuración del proyecto en el sistema es necesario asegurarse de que procesos anteriores no estén ejecutando, para esto se utilizan comandos de SystemD para detener estos procesos.

```bash
sudo systemctl start nginx.service
exit
```
