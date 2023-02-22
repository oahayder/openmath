FROM python:3.9

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
RUN export env/
COPY ./ .
RUN python3 main.py