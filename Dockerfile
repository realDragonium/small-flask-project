FROM python:3.7
COPY . /tmp/myapp
RUN pip install /tmp/myapp
CMD flask run