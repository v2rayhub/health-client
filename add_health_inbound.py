from app.proxyman.command.command_pb2 import AddInboundRequest
from app.proxyman.command.command_pb2_grpc import HandlerServiceStub

import grpc

# Create a channel and a stub
channel = grpc.insecure_channel('localhost:62789')
stub = HandlerServiceStub(channel)

print(stub.AddInbound(AddInboundRequest()))


