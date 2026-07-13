#!/usr/bin/env bash

pip install -r requirements.txt
python website/manage.py collectstatic --noinput
python website/ma nage.py migrate