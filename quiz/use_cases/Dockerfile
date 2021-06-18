FROM python:3.9.5-alphine3.13

COPY . /app
WORKDIR /app

RUN pip install pipenv

RUN pipenv install --system --deploy --ignore-pipfile

CMD ["python", "app.py"]