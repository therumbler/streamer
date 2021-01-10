import logging
import sys
from fastapi import FastAPI
from fastapi.responses import StreamingResponse, HTMLResponse
from .video import video_data

app = FastAPI()

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


@app.get("/")
async def index():
    """return static index.html"""
    with open("static/index.html") as f:
        return HTMLResponse(f.read())
    # return 'hi there'


@app.get("/stream")
async def stream(url: str):
    logger.info("stream endpoint")
    return StreamingResponse(video_data(url))
