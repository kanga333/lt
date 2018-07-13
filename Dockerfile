FROM python:3.6

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /app
COPY . /app/
WORKDIR /app

ENV FLASK_APP=run.py

ENTRYPOINT [ "/usr/local/bin/flask" ]
CMD [ "run" ]
