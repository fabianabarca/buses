# Developer Setup

Para poner a funcionar el proyecto localmente y poder desarrollar debemos seguir los siguientes pasos.
Requerimos de Python 3.7 o mayor, y un conjunto de paquetes que se descargan por medio del instalador
oficial, **pip**, en primer lugar debemos contar con estos programas en nuestro sistema operativo:

---

## Instalar Python y dependencias

### Ubuntu 18.04+/Debian

```bash
sudo apt update
sudo apt install python3 python3-pip
sudo pip3 install virtualenv
```

### Archlinux

```bash
sudo pacman -Sy python python-pip python-virtualenv
```

### Windows

En el caso de MS/Win puedes descargar Python desde la [web de los desarrolladores](https://www.python.org/downloads/windows/),
utilizando una versión mayor o igual a 3.7:

Una vez descargado damos doble click al instalador y acceso de administrador para que pueda colocarlo en el disco C:\\,
debemos asegurarnos de seleccionar la casilla de agregar Python al PATH. Continuamos con la instalación.

En Windows Python no se llama _python_ en consola, tiene el nombre de _py_, siempre que queramos hacer algo con Python debemos asegurarnos
de estar corriendo el comando _py_ de lo contrario no va a funcionar. Una vez termine la instalación posiblemente sea necesario reiniciar
la máquina para asegurar un funcionamiento correcto.

Podemos comprobar que _python_ ejecuta correctamente en nuestra sistema al abrir un _símbolo del sistema (cmd)_ o un PowerShell y ejecutar:

```powershell
py --version
```

Si al ingresar al símbolo del sistema o a PowerShell no tenemos el comando _py_ o el comando _python_ y en lugar de esto obtenemos un error
entonces debemos editar la variable **PATH** del sistema, esta configuración es bastante larga, por lo que se recomienda buscar el proceso en
internet, este [video de _YouTube_](https://www.youtube.com/watch?v=0bDRUOpec4c) muestra de una manera más sencilla como realizar esta configuración.

Una vez ya tenemos _python_ en nuestro sistema el comando pip también debería estar disponible en el símbolo del sistema o PowerShell.
Ejecutamos el siguiente comando para instalar virtualenv:

```powershell
pip install virtalenv
```
En Windows el comando pip no requiere permisos extra para editar archivos del sistema, pero si por alguna razón esta tarea llegara a fallar podemos cerrar
y abrir el PowerShell seleccionando click derecho **Abrir como administrador**.

---

## Clonar el repositorio

Desde una terminal nos dirigimos al lugar donde queremos que esté nuestro proyecto y ejecutamos el siguiente comando.

### Ubuntu 18.04+/Debian/Archlinux

```bash
git clone https://github.com/fabianabarca/buses.git
```

Si contamos con una cuenta _GitHub_ y esta ya está configurada con _SSH_ se recomienda el siguiente comando

```bash
git clone git@github.com:fabianabarca/buses.git
```

### Windows

En Windows _git_ no está instalado por defecto, para instalarlo debemos ir a la [web de los desarrolladores](https://git-scm.com/downloads)
descargamos el instalador y lo ejecutamos con permisos de administrador, una vez terminada la instalación tendremos en el sistema un
programa llamado _git-bash_, este es un terminal que ejecuta _Bash_, el Shell por defecto en Ubuntu/Debian, con este terminal podemos
ejecutar los comandos que no están disponibles en Windows por defecto. Se recomienda reiniciar el sistema para refrescar todas las variables
y configuraciones.

Si vamos al directorio donde queremos clonar el repositorio y damos click derecho en el área blanca del explorador de archivos veremos una nueva
opción, _abrir git-bash_, cuando damos click en esta opción nos abrirá una terminal. En esta terminal ejecutamos el siguiente comando:

```bash
git clone https://github.com/fabianabarca/buses.git
```
---

## Configurar un virtualenv

Ya con el virtualenv en nuestro sistema debemos asegurarnos de que la consola o la terminal estén en la ruta de nuestro proyecto,
el comando en todos los casos es el siguiente:

```sh
virtualenv venv
```

Esto va a crear un directorio llamado _venv_ que tendrá una copia de todas las bibliotecas base y de python para poder funcionar de manera
local sin tener que ensuciar o alterar la instalación en nuestro sistema.

Ahora para activar el ambiente virtual debemos ejecutar el siguiente comando:

### Ubuntu 18.04+/Debian/Archlinux

```bash
source ./venv/bin/activate
```

### Windows

En el caso de PowerShell
```powershell
venv\\Scripts\Activate.ps1
```

En el símbolo del sistema (cmd):
```cmd
venv\\Scripts\\activate.bat
```

En git-bash:
```bash
source ./venv/bin/activate
```

### Instalar las dependencias

Cuando ya tenemos el virtualenv activado podemos instalar localmente los requisitos del proyecto. Para esto debemos estar en el mismo sitio del proyecto
y ejecutar el comando **pip** de la siguiente forma:

```sh
pip install -r requirements.txt
```

Esto instalará todos los módulos que el proyecto necesita para levantar y funcionar en modo developer.

### Ejecutar el developer server

Ahora desde la misma terminal en que tenemos el virtualenv activado ejecutamos el siguiente comando:
```sh
python manage.py runserver
```
El fichero _manage.py_ debe encontrarse en el directorio sobre el cual estamos ejecutando el comando.

Este comando "no termina" es decir, la terminal se queda "pegada", pero no es que esté mal, esto
lo que significa es que el proceso se está ejecutando y la terminal se está usando para recibir e
imprimir la salida del programa, por ende el Shell o la línea de comandos ha quedado congelada en segundo plano.

Con esto último en la terminal nos saldrá un texto que indica la dirección en la cual podemos observar el proyecto.
http://localhost:8080

Si ingresamos desde el navegador veremos la página, ahora al editar código HTML, Javascript o Python en el directorio
del proyecto al guardarlo la página se va a refrescar mostrando los últimos cambios agregados.
