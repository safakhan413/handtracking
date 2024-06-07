# sudo apt-get install python # might need to update version # maybe python3 instead of python
# sudo apt install python3-pip
# pip3 install websockets
# run with python3, not python

# Steven's code copied and modified that can be used with Safa's

import websockets           # for web sockets
import asyncio              # used here - https://websockets.readthedocs.io/en/stable/intro.html#basic-example
import json                 # https://www.w3schools.com/python/python_json.asp
                            # sending data in json format lets us send as much data as we want and in any order
import time


key = '' # input both values here
domain = ''


async def connectSocket():
    url = domain+key
    async with websockets.connect(url) as websocket:
        print('websocket connected to ' + url)
        while True:
            direction = open('direction.txt').read()
            print(direction)
            if (direction == "up"):
                data = '{ "type": "GPIO", "pin": 4, "command": "HIGH" }';
                await websocket.send(data);
                data = '{ "type": "GPIO", "pin": 14, "command": "HIGH" }';
                await websocket.send(data);
            elif (direction == "down"):
                data = '{ "type": "GPIO", "pin": 15, "command": "HIGH" }';
                await websocket.send(data);
                data = '{ "type": "GPIO", "pin": 12, "command": "HIGH" }';
                await websocket.send(data);
            elif (direction == "left"):
                data = '{ "type": "GPIO", "pin": 4, "command": "HIGH" }';
                await websocket.send(data);
                data = '{ "type": "GPIO", "pin": 15, "command": "HIGH" }';
                await websocket.send(data);
            elif (direction == "right"):
                data = '{ "type": "GPIO", "pin": 12, "command": "HIGH" }';
                await websocket.send(data);
                data = '{ "type": "GPIO", "pin": 14, "command": "HIGH" }';
                await websocket.send(data);
            elif (direction == "none"):
                data = '{ "type": "GPIO", "pin": 4, "command": "LOW" }';
                await websocket.send(data);
                data = '{ "type": "GPIO", "pin": 12, "command": "LOW" }';
                await websocket.send(data);
                data = '{ "type": "GPIO", "pin": 14, "command": "LOW" }';
                await websocket.send(data);
                data = '{ "type": "GPIO", "pin": 15, "command": "LOW" }';
                await websocket.send(data);
            time.sleep(1)


# to edit the file
# open('direction.txt','w').write("up")
# open('direction.txt','w').write("none")


asyncio.get_event_loop().run_until_complete(connectSocket())
asyncio.get_event_loop().run_forever()




