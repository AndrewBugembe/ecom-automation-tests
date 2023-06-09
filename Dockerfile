FROM python:3.11

RUN apt update && apt install -y vim

#RUN mkdir /automation
##COPY requirements.txt /automation
##RUN python3 -m pip install /automation/requirements.txt
#
##option 2
WORKDIR /automation
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
COPY . .
