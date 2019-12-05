FROM python:3.7-alpine

RUN adduser -D validator

WORKDIR /home/validator

COPY requirements.txt requirements.txt
COPY setup.py setup.py
COPY ip_validator ip_validator

RUN pip install -r requirements.txt
RUN pip install -e .

COPY flask_app/app app
COPY flask_app/config.py flask_app/flask_app.py ./

ENV FLASK_APP flask_app.py

RUN chown -R validator:validator ./
USER validator

EXPOSE 5000

CMD python flask_app.py