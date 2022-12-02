#
FROM tiangolo/uwsgi-nginx-flask:python3.8

ENV NGINX_WORKER_PROCESSES auto

MAINTAINER tekrajchhetri@gmail.com
#
WORKDIR /code/

COPY ./requirements.txt /code/requirements.txt
RUN apt-get update && apt-get install -y ca-certificates
RUN pip3 install -r /code/requirements.txt
#
COPY ./ /code/app

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5070"]
