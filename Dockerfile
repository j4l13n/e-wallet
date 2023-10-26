# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /api
WORKDIR /api
ADD requirements.txt /api/
RUN pip install -r requirements.txt

ADD . /api/

# copy entrypoint.sh
ADD ./entrypoint.sh .
RUN sed -i 's/\r$//g' /api/entrypoint.sh
RUN chmod +x /api/entrypoint.sh

ENTRYPOINT ["/api/entrypoint.sh"]
