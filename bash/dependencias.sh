#!/bin/bash

# Lista de dependencias Python3 del ambiente virtual del proyecto
DEPENDENCIAS=(
    django
    gunicorn
    django-ckeditor
    pillow
)

# Comprobar o instalar dependencia
function python_dep ()
{
    # $1: Dependecia
    # Comprueba si la dependencia está instalada
    grep --ignore-case -c "$1" <<< "$( pip list | cut -f 1 -d ' ' )" &>/dev/null
    if (( $? ))
    then
        echo "Instalar la dependencia $1"
        pip3 install "$1"
        if (( $? ))
        then
            echo "Errores durante la instalación, revise sus permisos"
            exit 1
        fi
    else
        echo "La dependencia $1 ya se encuentra en el sistema"
    fi
}

## Instalar dependencias
for DEPENDENCIA in \
    ${DEPENDENCIAS[*]}
do
    python_dep $DEPENDENCIA
done

exit 0
