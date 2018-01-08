
FROM centos:7

RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y python-pip

ADD requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN mkdir /data

ADD dev /data

WORKDIR /data
EXPOSE 80
CMD ["/usr/bin/python", "/data/app.py"]