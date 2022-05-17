FROM python:3.8
RUN rm -rf /data/static
RUN rm -rf /usr/src/app
COPY /website/pages/static/ /data/static
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt