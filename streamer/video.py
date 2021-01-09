"""process a youtube-dl command"""
import asyncio
from asyncio.subprocess import PIPE
import logging


logger = logging.getLogger(__name__)


async def run(cmd):
    """run a shell command via asyncio"""
    proc = await asyncio.create_subprocess_shell(cmd, stdout=PIPE, stderr=PIPE)
    err = await proc.stderr.read()
    if err:
        logger.error(err)
    chunk = 1024 * 1024
    data = await proc.stdout.read(chunk)
    while data:
        yield data
        data = await proc.stdout.read(chunk)

    await proc.wait()
    logger.info("[%s exited with %d]", cmd, proc.returncode)


async def video_data(url):
    """asynchronous generator"""
    async for chunk in run(f"pipenv run youtube-dl --format mp4 -o - {url}"):
        yield chunk
