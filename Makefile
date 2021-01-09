run:
	pipenv run uvicorn streamer.web:app


build:
	docker build -t therumbler/streamer .


run-docker: build
	docker run -p ${PORT}:${PORT} therumbler/streamer