FROM binarin/docker-python3.4
ADD apt-requirements.txt /tmp/apt-requirements.txt
RUN apt-get install -y $(cat /tmp/apt-requirements.txt)
ADD python-requirements.txt /tmp/python-requirements.txt
RUN pip install -r /tmp/python-requirements.txt
EXPOSE 8000
