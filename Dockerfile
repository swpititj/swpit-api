FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD [ "python3", "main.py" ]
