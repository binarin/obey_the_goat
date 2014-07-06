FROM binarin/docker-python3.4
RUN pip install https://www.djangoproject.com/download/1.7c1/tarball/
RUN pip install selenium
EXPOSE 8000
