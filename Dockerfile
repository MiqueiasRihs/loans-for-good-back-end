FROM ubuntu
RUN addgroup --gid 1024 shared

WORKDIR /home/app

COPY . .
COPY locale.gen /etc/locale.gen

RUN apt-get update && \
	apt-get install sudo git nano curl gnupg build-essential libpq-dev \
	libjpeg8-dev zlib1g-dev libtiff-dev libfreetype6 libfreetype6-dev \
	libwebp-dev libopenjp2-7-dev -y python3-pip \
	&& pip install --no-cache-dir -r requirements.txt \
    && chmod +x setup_dev.sh

# Install Postgres
ARG DEBIAN_FRONTEND=noninteractive
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ jammy-pgdg main" >> /etc/apt/sources.list
RUN curl -fsSL "https://www.postgresql.org/media/keys/ACCC4CF8.asc" | gpg --dearmor > /etc/apt/trusted.gpg.d/postgres.gpg
RUN apt-get update && apt-get install postgresql-14 -y
RUN locale-gen

WORKDIR /tmp/
RUN sudo mv /etc/postgresql/14/main/pg_hba.conf /etc/postgresql/14/main/pg_hba.conf.bak
COPY pg_hba.conf /etc/postgresql/14/main/pg_hba.conf 

WORKDIR /home/app