from hello.grpc import hello_pb2_grpc
from hello.services import GreeterService


def grpc_handlers(server):
    hello_pb2_grpc.add_GreeterServicer_to_server(GreeterService(), server)
