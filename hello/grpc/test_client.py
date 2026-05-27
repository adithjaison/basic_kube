import asyncio

import grpc

from hello.grpc import hello_pb2, hello_pb2_grpc


async def main():
    async with grpc.aio.insecure_channel('localhost:50051') as ch:
        stub = hello_pb2_grpc.GreeterStub(ch)
        resp = await stub.SayHello(hello_pb2.HelloRequest(name='world'))
        print(resp.message)


if __name__ == '__main__':
    asyncio.run(main())
