# Author: Yjj
# -*- coding: utf-8 -*-

'''
async web application.
'''

import logging
import asyncio, os, json, time
from aiohttp import web
from datetime import datetime

logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', headers={'content-type': 'text/html'})


async def init(loop):
    # app = web.Application(loop=loop)
    app = web.Application()
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app._make_handler(), '127.0.0.1', 9011)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
