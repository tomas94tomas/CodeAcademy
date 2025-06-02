FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3
ENV MESSAGE="Hello from ENV"
COPY hello.py .

CMD ["python3", "hello.py"]