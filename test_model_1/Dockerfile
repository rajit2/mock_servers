FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim


COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /app
COPY . /app
