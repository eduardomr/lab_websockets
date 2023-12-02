import asyncio
import websockets

all_clients = []


async def send_message(message: str, sender):
    for client in all_clients:
        if client != sender:
            await client.send(message)


async def new_client_connected(client_socket, path):
    print("Novo cliente conectado!")
    all_clients.append(client_socket)

    while True:
        new_message = await client_socket.recv()
        print(f"Mensagem recebida: {new_message}")
        await send_message(new_message, client_socket)


async def start_server():
    print("Servidor iniciado!")
    await websockets.serve(new_client_connected, "localhost", 12345)


if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(start_server())
    event_loop.run_forever()