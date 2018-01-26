FROM library/python:3.6
 
RUN pip install locustio \
 && mkdir /locust

ADD . /locust

WORKDIR /locust

EXPOSE 8089
ENTRYPOINT [ "locust" ]
