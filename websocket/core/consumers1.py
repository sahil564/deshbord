from http import client
import paho.mqtt.client as paho
import time
from django.shortcuts import render
import json
from multiprocessing import Event
from asgiref.sync import async_to_sync, sync_to_async

from time import sleep
import asyncio
from channels.consumer import SyncConsumer,AsyncConsumer


# Create your views here.

sa=[]
def onMessage(clinet,userdata,msg):
    
    s=msg.payload.decode()
    sa.append(s)
    print(msg.topic+": "+ msg.payload.decode())

client=paho.Client()
client.on_message=onMessage

client.connect("3.16.216.28",1883,60)


client.subscribe("test")

client.loop_start()


while True:
    time.sleep(1)
    data=sa
    class MyAsyncConsumer(AsyncConsumer):
        # this is handler is called when client initailly opns a
        #connetions and is about to finish the webSocket handshake
        async def websocket_connect(self,evet):
            print("Websocket Connected...")
            await self.send({
             'type':"websocket.accept"
            })
         
        #this handler is called when data received from client     
        async def websocket_receive(self,event):
            print("message Received forn asyc..")
            print("type of recieved data ",type(event['text']))
            while True:
                await self.send({'type':'websocket.send',
                'text':str(data)
                })
                await asyncio.sleep(1)
                
          
            #this handler is called when either connection to the client is lost either from the client closing the connection the server
            #closing the connection or loss of the socket   
            async def websocket_disconnect(self,event):
                print("Websocket Disconnected..")


    def sahil(request):
        if len(sa)<=1:
            return render(request,"/home/sahil/Desktop/websocket/core/templates/app/index1.html",{"data":data})
        else:
            return render(request,"/home/sahil/Desktop/websocket/core/templates/app/index1.html",{"data":data[-1][0]})

    break
    