FROM python:3.11

RUN apt update && apt install -y vim
# Update package lists and install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    curl

# Install Chrome




##COPY requirements.txt /automation
##RUN python3 -m pip install /automation/requirements.txt
#
##option 2

#COPY requirements.txt .
#RUN python3 -m pip install -r requirements.txt
#COPY . .
#WORKDIR /automation/shoppingtests/tests/frontend/myaccount
#ENTRYPOINT ["python3", "-m", "pytest"]
##ENTRYPOINT ["python3", "-m", "pytest", "tests"]
