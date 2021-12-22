import asyncio

import aiohttp

__all__ = []


async def send_private_msg(user_id, group_id, message, auto_escape=False):
    # user_id, group_id, message, auto_escape
    data = {'user_id': user_id,
            'group_id': group_id,
            'message': message,
            'auto_escape': auto_escape}
    async with aiohttp.ClientSession() as session:
        async with session.post('/send_private_msg', data=data) as response:
            if response.status != 200:
                pass  # todo
