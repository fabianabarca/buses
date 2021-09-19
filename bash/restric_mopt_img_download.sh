#!/bin/bash

IMAGE_URL="$(
    wget -O - --quiet --no-check-certificate 'https://www.mopt.go.cr/wps/portal/Home/informacionrelevante/restriccion/' |
        grep '<img[^>]*[^>]*>' -o |
        grep 'restricci[[=o=]]n' -i |
        grep -o 'src="[^"]*' |
        sed 's/src="/https:\/\/www.mopt.go.cr/'
         )"

echo "Restricción imagen URL: $IMAGE_URL"

wget --quiet --no-check-certificate -O restric.png "$IMAGE_URL"

exit 0
