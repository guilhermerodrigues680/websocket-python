# WS client
# pip install websockets
#Here’s a WebSocket server example.
#It reads a name from the client, sends a greeting, and closes the connection.

import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:
        name = input("What's your name? ")
        
        # envia dado pela porta
        await websocket.send(name)
        print(f"Enviado: > {name}")

        # recebe dado pela porta
        greeting = await websocket.recv()
        print(f"Recebido: < {greeting}")

asyncio.get_event_loop().run_until_complete(hello())