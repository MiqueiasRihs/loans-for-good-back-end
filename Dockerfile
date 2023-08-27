FROM python:3

WORKDIR /home/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt \
    && chmod +x setup_dev.sh
