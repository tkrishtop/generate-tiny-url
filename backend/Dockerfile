FROM python:3.8

LABEL org.opencontainers.image.authors="Tatiana KRISHTOP"
LABEL com.github.version="0.0.1"

ENV APP_ROOT /app

# copy everything into tmp folder
COPY . ${APP_ROOT}

# go into the destination directory
WORKDIR ${APP_ROOT}

# install requirements
RUN pip install -r ${APP_ROOT}/requirements.txt

# run the application
EXPOSE 5555
CMD ["uwsgi", "--socket", "0.0.0.0:5555", "--protocol=http", "-w", "wsgi:app", "--logto", "/var/log/uwsgi.log"]