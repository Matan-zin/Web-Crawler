FROM alpine:3.17.1


RUN apk update && apk add python3 openrc py-pip 
RUN pip3 install PySocks
RUN pip3 install python-dateutil
RUN crond

WORKDIR /Crawler

COPY . .

RUN chmod a+x /Crawler/crawler.py

RUN echo "0 */4 * * * /Crawler/crawler.py" >> /etc/crontabs/root

RUN python3 /Crawler/database/init_db.py

CMD ["tail", "-f", "/dev/null"]