# Chat html com WebSocket e servidor programado em Python
# Autor: Guilherme Rodrigues
# Data: 02/07/2019

import asyncio
import json
#import logging
import websockets

# (Um set é um conjunto nao ordenado e nao indexado, assim não há como haver elementos repetidos)
USUARIOS = set() # Cria um conjunto de dados vazio.

async def chat_main(websocket, path):
    USUARIOS.add(websocket)
    try:
        async for dado in websocket:
            print('Recebi: ' + dado)
            s = 'Servidor: ' + dado
            #await websocket.send(s)
            await asyncio.wait( [usuario.send(s) for usuario in USUARIOS] )
    finally:
        USUARIOS.remove(websocket)
        print('Finally')

asyncio.get_event_loop().run_until_complete( websockets.serve(chat_main, 'localhost', 5678) )
asyncio.get_event_loop().run_forever()