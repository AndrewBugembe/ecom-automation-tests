FROM python:3.11

RUN mkdir /automation
#COPY requirements.txt /automation
#RUN python3 -m pip install /automation/requirements.txt

#option 2
WORKDIR /automation
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
