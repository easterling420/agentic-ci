#!/bin/bash
cd "$(dirname "$0")/ui"
gunicorn -w 2 -b 0.0.0.0:8000 app:app
