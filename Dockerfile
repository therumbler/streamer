FROM python:3.8

WORKDIR /app

RUN pip3 install pipenv

EXPOSE 8080

COPY Pipfile* ./
RUN pipenv sync

COPY . ./

RUN ls -la ./


CMD [ "pipenv", "run", "uvicorn", "--host", "0.0.0.0", "--port", "8080", "streamer.web:app"]