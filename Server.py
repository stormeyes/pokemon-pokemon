import time
import grpc
import Config
import Logic
from concurrent import futures
from proto import pokemon_pb2_grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=Config.SERVER_MAX_WORKERS), options=[
        ('grpc.max_send_message_length', Config.SERVER_MAX_SEND_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', Config.SERVER_MAX_RECEIVE_MESSAGE_LENGTH)])

    pokemon_pb2_grpc.add_PokemonServicer_to_server(Logic.RequestRpc(), server)
    server.add_insecure_port(Config.SERVER_ADDR)
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)  # one day in seconds
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
