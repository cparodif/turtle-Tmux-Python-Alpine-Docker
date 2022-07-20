FROM python:3.11-rc-alpine
MAINTAINER Carlos Parodi (cparodif)
RUN mkdir -p /turtle  \
    && apk update &&  apk upgrade  \
    && apk add --update --no-cache  bash curl zip \
    && apk add --update --no-cache  tk python3-tkinter  \
    && apk add -U tzdata \
    && cp /usr/share/zoneinfo/Europe/Madrid /etc/localtime \
    && echo "Europe/Madrid" > /etc/timezone \
    && apk del tzdata \
    && cd /turtle \
    && apk add --update --no-cache  nano mc  tmux htop\
    && apk add --update --no-cache font-misc-misc font-vollkorn terminus-font \
    && rm -rf /var/cache/apk/*  /tmp/*   
WORKDIR /turtle
COPY --chown=root:root  entrypoint.sh /
COPY --chown=root:root  ./ /turtle/
RUN   chmod +x /entrypoint.sh 
RUN   chmod +x /turtle/* 
ENV DISPLAY :0
ENTRYPOINT ["/entrypoint.sh"]
