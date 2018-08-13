FROM ubuntu:18.04

RUN apt-get install -qy python3

RUN pip-3.3 install -r requirements.txt
