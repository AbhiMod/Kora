FROM python:3.10-slim-buster

WORKDIR /app

RUN apt-get -y update && apt-get -y install git gcc python3-dev ffmpeg tini

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN pip3 install python-telegram-bot==13.5

RUN pip3 install urllib3==1.26.15 

RUN pip3 install requests-toolbelt==0.10.1

COPY . .

ENTRYPOINT ["/usr/bin/tini", "--"]

CMD [ "python", "kora.py"]
