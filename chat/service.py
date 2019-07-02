#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-07-02 09:17:35


import logging
from channels.layers import get_channel_layer

log = logging.getLogger("default")
channel_layer = get_channel_layer()


class MySignal(object):

    async def onconnect(self, group_name):
        log.info("MySignal.onconnect")
        await channel_layer.group_send(
            # group_name,
            "chat_room",
            {
                'type': 'chat_message',
                'message': f"有人加入了{group_name}",
            }
        )
