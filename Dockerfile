FROM alpine:3.16

RUN apk add --update py3-pip
WORKDIR /app/

COPY . /app/
COPY cronjob /var/spool/cron/crontabs/root

RUN pip3 --no-cache-dir install -r requirements.txt
RUN chmod 0655 /app/src/main.py



CMD crond -l 2 -f