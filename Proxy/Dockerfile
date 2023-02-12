FROM alpine:3.17.1


RUN apk update && apk add tor

RUN mkdir -p /etc/tor

RUN echo 'SocksPort 0.0.0.0:9050' > /etc/tor/torrc

RUN chown -R tor /etc/tor

USER tor

ENTRYPOINT ["tor"]

CMD ["-f", "/etc/tor/torrc"]
