# Dockerfile

FROM python:3.8

ADD herg_docker.py

RUN pip install numpy pandas pyjanitor pickle5

CMD ["python", "./herg_docker.py"]