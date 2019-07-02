# WS server
# pip install websockets
#Here’s a WebSocket server example.
#It reads a name from the client, sends a greeting, and closes the connection.

import asyncio
import websockets

async def hello(websocket, path):
    # recebe dado pela porta
    nome = await websocket.recv()
    print(f"Recebido: < {nome}")

    msg = f"Hello {nome}!"
    # envia dado pela porta
    await websocket.send(msg)
    print(f"Enviado: > {msg}")

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()