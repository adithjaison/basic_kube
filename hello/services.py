from hello.grpc import hello_pb2, hello_pb2_grpc


class GreeterService(hello_pb2_grpc.GreeterServicer):
    async def SayHello(self, request, context):
        return hello_pb2.HelloResponse(message=f"Hello, {request.name}!")
