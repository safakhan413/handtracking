import websockets
import asyncio
import json
import time

key = "5fa89a529623b645aa04690b"
domain = "wss://remotescontrol1.herokuapp.com/"

async def connectSocket():
    url = domain + key
    async with websockets.connect(url) as websocket:
        print('WebSocket connected to ' + url)
        while True:
            direction = open('direction.txt').read().strip()
            print(f'Direction: {direction}')
            if direction == "up":
                data = [
                    { "type": "GPIO", "pin": 4, "command": "HIGH" },
                    { "type": "GPIO", "pin": 14, "command": "HIGH" }
                ]
            elif direction == "down":
                data = [
                    { "type": "GPIO", "pin": 15, "command": "HIGH" },
                    { "type": "GPIO", "pin": 12, "command": "HIGH" }
                ]
            elif direction == "left":
                data = [
                    { "type": "GPIO", "pin": 4, "command": "HIGH" },
                    { "type": "GPIO", "pin": 15, "command": "HIGH" }
                ]
            elif direction == "right":
                data = [
                    { "type": "GPIO", "pin": 12, "command": "HIGH" },
                    { "type": "GPIO", "pin": 14, "command": "HIGH" }
                ]
            elif direction == "none":
                data = [
                    { "type": "GPIO", "pin": 4, "command": "LOW" },
                    { "type": "GPIO", "pin": 12, "command": "LOW" },
                    { "type": "GPIO", "pin": 14, "command": "LOW" },
                    { "type": "GPIO", "pin": 15, "command": "LOW" }
                ]

            # Send all data commands
            for cmd in data:
                await websocket.send(json.dumps(cmd))
            
            # Sleep for a short time before checking the direction again
            time.sleep(0.1)

# to edit the file
# open('direction.txt','w').write("up")
# open('direction.txt','w').write("none")

asyncio.get_event_loop().run_until_complete(connectSocket())
asyncio.get_event_loop().run_forever()
