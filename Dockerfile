FROM python:3

WORKDIR /home/app/

COPY .env .
COPY entrypoint.sh .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && chmod +x entrypoint.sh

CMD ["chmod +x entrypoint.sh"]
