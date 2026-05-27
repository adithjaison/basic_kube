#!/usr/bin/env bash



/usr/local/bin/daphne -b 0.0.0.0 -p 8000 --access-log - --proxy-headers basic_kube.asgi:application