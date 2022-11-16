from channels.generic.websocket import AsyncWebsocketConsumer
import json
from random import randint
from asyncio import sleep

class GraphConsumer11(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        data=[72,69,69,69,69,69,69, 69,69,69,69,70,72,71,73,72,69,69,69, 69,69,69,70,69,69,109,70,69,71,73]
        for i in data:
            await self.send(json.dumps({'value':i}))
            await sleep(1)
            
            
            
class GraphConsumer111(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        data=[2000,2200,2100,2189,2100,2121,2189,2300,2400,2300,2201,2170,2272,2299,2373,2072,2269,2369,2369,2399,2169,2369,2209,4500,2269,2169,2270,2372,2199,2390]
        for i in data:
            await self.send(json.dumps({'value':i}))
            await sleep(1)

class GraphConsumer21(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        data=[200,220,210,289,210,221,289,230,240,200,201,270,272,299,233,272,269,239,269,239,219,239,209,400,229,269,220,272,219,200]
        for i in data:
            await self.send(json.dumps({'value':i}))
            await sleep(1)
class GraphConsumer31(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        data=[200,220,210,289,210,221,289,230,240,200,201,270,272,299,233,272,269,239,269,239,219,239,209,600,229,269,220,272,219,200]
        for i in data:
            await self.send(json.dumps({'value':i}))
            await sleep(1)
class GraphConsumer41(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        data=[200,220,210,289,210,221,289,230,240,200,201,270,272,299,233,272,269,239,269,239,219,239,209,700,229,269,220,272,219,200]
        for i in data:
            await self.send(json.dumps({'value':i}))
            await sleep(1)