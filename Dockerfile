FROM ubuntu:latest
LABEL authors="bugie"

ENTRYPOINT ["top", "-b"]