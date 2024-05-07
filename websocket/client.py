#!/usr/bin/env python

import asyncio
import websockets

host = 'localhost'
port = '1234'

async def echo():
    uri = "ws://" + host + ':' + port + "/echo"
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("Input a string: ")

            await websocket.send(message)
            print(f">>> {message}")

            receive = await websocket.recv()
            print(f"<<< {receive}")


if __name__ == "__main__":
    asyncio.run(echo())