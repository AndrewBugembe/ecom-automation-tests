FROM python:3.11
RUN apt update && apt install -y vim

# INSTALLING HEADLESS CHROME
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -y google-chrome-stable

RUN mkdir /automation
WORKDIR /automation/shoppingtests
COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt
COPY . .
#in the entrypoint, use can use a scriptwith the commands to run the tests just like script for variables
