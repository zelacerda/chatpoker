FROM alpine:3.17

RUN apk update \
    && apk add python3

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY ./*.py ./

CMD ["python3", "poker.py"]