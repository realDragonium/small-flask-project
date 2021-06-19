FROM python:3.9.5-slim

COPY . /app
WORKDIR /app

RUN pip install pipenv

RUN pipenv install --deploy --ignore-pipfile

CMD ["python", "-m", "unittest", "discover", "-v"]