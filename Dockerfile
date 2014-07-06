FROM binarin/docker-python3.4
RUN pip install https://www.djangoproject.com/download/1.7c1/tarball/
RUN pip install selenium
RUN apt-get install -y libpq-dev
RUN pip install psycopg2
EXPOSE 8000
