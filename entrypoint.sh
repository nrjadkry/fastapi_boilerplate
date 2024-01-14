#!/bin/bash

NAME=fastapi-boilerplate
DIR=/code
USER=fastapi
GROUP=fastapi
WORKERS=4
WORKER_CLASS=uvicorn.workers.UvicornWorker
LOG_LEVEL=error

cd $DIR

uvicorn app.main:app --host 0.0.0.0 --port 8001 --workers 4