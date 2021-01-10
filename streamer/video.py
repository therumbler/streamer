"""process a youtube-dl command"""
import asyncio
from asyncio.subprocess import PIPE
import logging


logger = logging.getLogger(__name__)


async def run(cmd):
    """run a shell command via asyncio"""
    logger.info('running %s', cmd)
    proc = await asyncio.create_subprocess_shell(cmd, stdout=PIPE, stderr=PIPE)
    chunk = 1024 * 1024
    logger.debug('getting stdout...')
    data = await proc.stdout.read(chunk)
    if not data:
        logger.error('no stdout data')
    while data:
        yield data
        data = await proc.stdout.read(chunk)

    await proc.wait()
    logger.info("[%s exited with %d]", cmd, proc.returncode)
    err = await proc.stderr.read()
    if err:
        logger.error(err)


async def video_data(url):
    """asynchronous generator"""
    async for chunk in run(f"youtube-dl --format mp4 -o - {url}"):
        yield chunk
