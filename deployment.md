# <img src="https://www.blueprism.com/uploads/assets/icons/deployment_2020-10-21-214701.svg" width="60"> Deployment - full setup

En desarrollo web el deployment es el momento en el que colocamos nuestro código a disposición del equipo, e infraestructura del proyecto, en general se hace con la idea de evaluar la integración del software con los demás elementos a los cuales este debe servir, la mayor parte de la veces el deployment consiste en publicar de cierta forma el programa y ponerlo a funcionar como este normalmente lo haría en producción, en un servidor ya sea público o privado pero al cual las personas y servicios que nos interesan tengan acceso.

## Publicar este proyecto utilizando la CLI <img src="https://i0.wp.com/urlanheat.com/blog/wp-content/uploads/2016/07/logo-bash.png" height="50">

Lo primero que se debe hacer es entrar en una terminal con Bash o cualquier otro shell que sea POSIX.
Nos conectamos al servidor en el cual queremos montar el proyecto, para esto usamos ssh:

```bash
ssh -l nombre 10.20.30.40
```

**nombre** es la cuenta que tenemos en ese servidor, y la IP debe ser la del servidor.

Para mayor orden creamos un directorio en el cual colocar el proyecto y clonamos el estado actual del proyecto con **git**

```bash
mkdir deployment-$(date +'%d-%m-%y')
cd deployment-$(date +'%d-%m-%y')

git clone https://github.com/fabianabarca/buses.git
cd buses
```

Actualizamos el sistema host (en este caso Ubuntu) para instalar las dependencias necesarias

```bash
sudo apt update
sudo apt upgrade
sudo apt install python3.7 python3-pip virtualenv python3-virtualenv

python --version
```

Nuestra versión de Python debe ser idealmente mayor o igual a la 3.7, si no lo es debemos actualizar este software, ya sea desde el sitio o repositorio oficial. Es posible también que el python por default sea 3.6 o menor, en ese caso en lugar de usar python podemos usar python3.7


El proyecto cuenta con un script de configuración que autogenera los ficheros de configuración, para ejecutarlo lo hacemos de la siguiente forma

```bash
./config
```

El script levantará el virtualenv y pondrá en el root del proyecto los dos ficheros necesarios para levantar el servidor

Si ya teníamos una versión anterior del proyecto es necesario decirle al servidor que debe detener el servicio de _NGINX_ y _GUNICORN_ (más adelante veremos como usando SysD)

### Configurar el proyecto para operar en red

Es necesario indicar a Django que _nombres_ o IPs son válidos para referirse al servidor, a sí mismo, en una petición. Para cambiar los ALLOWED_HOSTS debemos cambiar esta línea en el fichero de configuración del proyecto, settings.py, colocar dentro de esta la URL o la IP de nuestro servidor, como un STRING, ejemplo:

```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["10.20.30.40"]

```

Es importante también colocar la constante _DEBUG_ en False para evitar logs e información que pueda vulnerar el sitio si este no se encuentra en una red protegida.

### Habilitar el correo

Para que el contact form del proyecto pueda recibir y enviar correos el mismo debe de registrarse ante algún servicio de correo, ya sea local o externo, en este caso a manera de ejemplo se puede configurar para que utilice una cuenta de Gmail colocando lo siguiente en la configuración del sitio, _settings.py_

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'cuenta@gmail.com'
EMAIL_HOST_PASSWORD = 'clave'
```

Con esto a la hora de hacer un **POST** en la página de contacto se recibirá una confirmación por correo de que nuestro mensaje ha sido enviado a bandeja.

### Usar estilos de aplicaciones de Django y de terceros

Tanto las aplicaciones de Django como las de terceros encapsulan su propio _/static/_ en el cual almacenan sus ficheros de JavaScript y CSS, estos se pueden ver correctamente cuando levantamos el servidor de desarrollo que viene con el framework, pero una vez que usamos el _WSGI_ en conjunto con _NGINX_ notaremos que las aplicaciones externas perderán sus estilos e interacciones de JavaScrip, esto sucede porque en producción no es sensato hacer peticiones de ficheros estáticos a través de un servición o rutina dinámica, por eso se espera que por parte del usuario se coloquen estos estilos y scripts en el directorio estático correspondiente al propio proyecto, este contenido será servido directamente por NGINX.

### Levantar el servicio 

<img src="https://luiszambrana.com.ar/wp-content/uploads/2020/06/logo-nginx-luiszambrana.png" height="70">
Así como especificamos la IP permitida en el settings.py es necesario colocar el correcto **server\_name** en la configuración de Nginx, para esto editamos el fichero llamado _web-buses.nginx-config_ en el encontraremos dicha sección, ahí se colocará la URL del sitio o la IP en su defecto.

Antes de posicionar los ficheros de configuración del proyecto en el sistema es necesario asegurarse de que procesos anteriores no estén ejecutando, para esto se utilizan comandos de SystemD para detener estos procesos.

<img src="https://cdn.worldvectorlogo.com/logos/gunicorn.svg" height="70">

```bash
sudo systemctl stop gunicorn.service
sudo systemctl stop nginx
```

Ahora podemos colocar los nuevos ficheros de configuración en su lugar, para esto se puede colocar manualmente el gunicorn en SystemD y el web-buses.nginx en la configuración de Nginx, el script de configuración es capaz de hacerlo también con el siguiente comando

```bash
sudo ./config install
```
Una vez instalado los ficheros y habilidados los servicios es posible observar el sitio al introducir la IP del servidor en el navegador, de la siguiente forma, http://IP-DEL-SERVIDOR/ se debe utilizar http ya que el proyecto no cuenta con firma SSL.

Cualquier problema con el procedimiento coméntelo con el equipo en el respectivo canal de discusión.

## Publicar este proyecto con ayuda de Docker (próximamente)

## Publicar este proyecto por interfaz gráfica (próximamente)
