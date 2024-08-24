#!/usr/bin/env sh

if [ -z "${IMAGE_URL}" ]; then
  echo "ERROR: Env var IMAGE_URL missing"
  sleep 30
  exit 1
fi

while true; do
    python main.py ${IMAGE_URL} /out/data --crop-top ${CROP_TOP:-0} --timeline ${TIMELINE:-3600} --threshold ${TRESHOLD:-100}
    echo "sleep ${UPDATE_INTERVAL_IN_SECONDS:-3600}"
    sleep ${UPDATE_INTERVAL_IN_SECONDS:-3600}
done
