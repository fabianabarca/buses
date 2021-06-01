# Deployment - full setup
<img src="https://www.blueprism.com/uploads/assets/icons/deployment_2020-10-21-214701.svg" width="150">

En desarrollo web el deployment es el momento en el que colocamos nuestro código a disposición del equipo, e infraestructura del proyecto, en general se hace con la idea de evaluar la integración del software con los demás elementos a los cuales este debe servir, la mayor parte de la veces el deployment consiste en publicar de cierta forma el programa y ponerlo a funcionar como este normalmente lo haría en producción, en un servidor ya sea público o privado pero al cual las personas y servicios que nos interesan tengan acceso.

## Publicar este proyecto utilizando la CLI

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

Si ya teníamos una versión anterior del proyecto es necesario decirle al servidor que debe detener el servidor

### Configurar el proyecto para operar en red

Es necesario indicar a Django que _nombres_ o IPs son válidos para referirse al servidor, a sí mismo, en una petición. Para cambiar los ALLOWED_HOSTS debemos cambiar esta línea en el fichero de configuración del proyecto, settings.py, colocar dentro de esta la URL o la IP de nuestro servidor, como un STRING, ejemplo:

```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["10.20.30.40"]

```

Es importante también colocar la constante _DEBUG_ en False para evitar logs e información que pueda vulnerar el sitio si este no se encuentra en una red protegida.

### Usar estilos de aplicaciones de Django y de terceros

TODO

### Levantar el servicio

```bash
sudo systemctl stop gunicorn.service
sudo systemctl stop nginx
```

Ahora podemos colocar los nuevos ficheros de configuración en su lugar, para esto se puede colocar manualmente el gunicorn en SystemD y el web-buses.nginx en la configuración de Nginx, el script de configuración es capaz de hacerlo también con el siguiente comando

```bash
sudo ./config install
```


## Publicar este proyecto por interfaz gráfica (próximamente)
