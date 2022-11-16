from channels.generic.websocket import AsyncWebsocketConsumer
import json
from random import randint
from asyncio import sleep

class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
        for i in range(1000):
            await self.send(json.dumps({'value':randint(79,100)}))
            await sleep(1)
            
            
            
class GraphConsumer1(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
        for i in range(1000):
            await self.send(json.dumps({'value':randint(2000,2500)}))
            await sleep(1)

class GraphConsumer2(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
        for i in range(1000):
            await self.send(json.dumps({'value':randint(200,300)}))
            await sleep(1)
class GraphConsumer3(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
        for i in range(1000):
            await self.send(json.dumps({'value':randint(200,300)}))
            await sleep(1)
            
class GraphConsumer4(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
        for i in range(1000):
            await self.send(json.dumps({'value':randint(200,300)}))
            await sleep(1)