FROM python:3.8-alpine

ENV REDIS_PW = "root"

COPY . /code

WORKDIR /code

RUN pip install -r requirements.txt

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
