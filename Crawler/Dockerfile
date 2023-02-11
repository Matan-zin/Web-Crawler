FROM alpine:3.17.1


RUN apk update && apk add python3
RUN rc-service crond start && rc-update add crond

WORKDIR /Crawler

COPY . .

RUN echo "0 */4 * * * /Crawler/crawler.py" >> var/spool/cron/crontabs/root


CMD ["python3", "/Crawler/crawler.py"]