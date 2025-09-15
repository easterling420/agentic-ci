#!/bin/bash
export PYTHONPATH=$PWD

cd "$(dirname "$0")/ui"
gunicorn -w 1 -t 2 --timeout 60 -b 0.0.0.0:8000 app:app
