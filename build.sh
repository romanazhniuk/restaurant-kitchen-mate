#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
# Render often does not set RENDER during build; DEBUG must be False for WhiteNoise manifest storage.
export RENDER=true
python manage.py collectstatic --no-input
python manage.py migrate
