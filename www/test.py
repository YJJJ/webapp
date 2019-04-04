import asyncio

import sys

import www.orm as orm
from www.models import User, Blog, Comment


async def test(loop):
    await orm.create_pool(loop=loop, host='127.0.0.1', user='root', password='123456', db='awesome')

    u = User(name='Test', email='yjj6@example.com', passwd='123456', image='about:blank')

    await u.save()
    await orm.destory_pool()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
# if loop.is_closed():
#     sys.exit()
