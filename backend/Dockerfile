FROM python:3.8-alpine as builder

RUN    apk add                  \
        build-base              \
        linux-headers           \
        pcre-dev                \
        python3-dev             \
    && python -m venv /.venv    \
    && . /.venv/bin/activate    \
    && pip install              \
        flask                   \
        pytest                  \
        uwsgi                   \
        wtforms

FROM python:3.8-alpine

LABEL org.opencontainers.image.authors="Tatiana KRISHTOP"
LABEL com.github.version="0.0.1"

COPY . /app
COPY --from=builder /.venv /.venv

RUN apk add pcre

WORKDIR /app
ENTRYPOINT ["/app/entrypoint.sh"]