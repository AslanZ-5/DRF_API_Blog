FROM python:3.8-slim-buster
ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN python -m pip install -r requirements.txt
RUN apk del .tmp

RUN mkdir /app_blog
COPY . /app_blog
WORKDIR /appw
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static


RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user 

CMD [ "entrypoint.sh" ]