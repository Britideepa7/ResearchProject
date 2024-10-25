FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY highavailability.py random-mqtt.py publisher.py subscriber.py ./

ENV PYTHONUNBUFFERED=1

ARG SCRIPT_NAME

CMD ["sh", "-c", "python3 $SCRIPT_NAME"]
