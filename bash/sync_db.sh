#!/bin/bash

set -e

./manage.py makemigrations
./manage.py migrate --run-syncdb

exit 0
