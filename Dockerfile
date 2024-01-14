FROM python:3.9-slim-bullseye

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --upgrade pip  && pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/

ENTRYPOINT [ "sh", "/code/entrypoint.sh" ]