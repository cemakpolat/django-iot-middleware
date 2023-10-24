#!/bin/bash
python3 manage.py makemigrations &&
python3 manage.py migrate &&
gunicorn --bind 0.0.0.0:8000 device_manager.asgi -w 1 -k uvicorn.workers.UvicornWorker
    