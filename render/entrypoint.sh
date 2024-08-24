#!/usr/bin/env bash

while true; do
    /usr/local/bin/esp-render /config.json /out/data.img
    sleep ${UPDATE_INTERVAL_IN_SECONDS:-3600}
done
