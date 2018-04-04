FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD /config/requirements.pip /config/
RUN pip install -r /config/requirements.pip
RUN mkdir /src;
WORKDIR /src
RUN apt-get update \
&& apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info -y

