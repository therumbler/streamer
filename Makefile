run:
	pipenv run uvicorn --host 0.0.0.0 --log-level debug streamer.web:app


build:
	docker build -t therumbler/streamer .


run-docker: build
	docker run -p ${PORT}:${PORT} therumbler/streamer
