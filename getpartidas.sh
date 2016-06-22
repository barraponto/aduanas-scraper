#!/usr/bin/env bash

for tipo in `cat tipos.txt`; do echo $tipo; sudo kill -HUP `pidof tor`; casperjs --ignore-ssl-errors=true --proxy=127.0.0.1:9050 --proxy-type=socks5 02-partidas.js --tipo=$tipo; done
