
FROM ubuntu:14.04

MAINTAINER Arne Neumann <nlpdocker.programming@arne.cl>

RUN apt-get update
RUN apt-get install -y git python3-pip

RUN pip3 install django

WORKDIR /opt
RUN git clone https://github.com/amagidow/dialects.git

RUN apt-get update
RUN apt-get install -y libpq-dev
RUN apt-get install -y binutils libproj-dev gdal-bin
RUN apt-get install -y postgresql

WORKDIR /opt/dialects
COPY requirements.txt /opt/dialects/
COPY localsettings.py /opt/dialects/dialects/
RUN LC_ALL=C.UTF-8 pip3 install -r requirements.txt

RUN service postgresql start && sudo -u postgres psql -c "alter user postgres with password 'postgres';"

CMD service postgresql start && DIALECTDBSK=postgres python3 manage.py runserver
