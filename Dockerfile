FROM centos/python-36-centos7

USER root

RUN yum install -y mysql

COPY ./mainsite /mainsite
COPY requirements.txt /mainsite
COPY run.sh /mainsite

WORKDIR /mainsite
RUN pip install -r requirements.txt

#EXPOSE 8000

#CMD sleep infinity
#CMD python manage.py runserver