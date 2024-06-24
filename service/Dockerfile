FROM python:3.12

WORKDIR /opt/link_dst/service
COPY requirements.txt requirements.txt

RUN chmod +x .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .
