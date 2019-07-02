#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-12-10 19:07:24


# chat/consumers.py
# chat/consumers.py
import logging
from channels.layers import get_channel_layer
from channels.generic.websocket import AsyncWebsocketConsumer
from . import service
import json


log = logging.getLogger("default")


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        log.info("有人链接了{}".format(self.channel_name))
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        log.info("加入group")
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        channel_layer = get_channel_layer()
        log.info("发送消息")
        await channel_layer.send(  # 可以直接给某个channel_name发送消息
            self.channel_name, {"type": "chat.message", "message": "Hello there!"})
        log.info("触发回调")
        signal = service.MySignal()
        await signal.onconnect(self.room_group_name)

    async def disconnect(self, close_code):
        # Leave room group
        log.info("用户关闭了链接: code: {}".format(close_code))  # 如果用户close的时候没有输入code, 这里就是None
        log.info("关闭链接")
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
