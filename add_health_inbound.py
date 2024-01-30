from app.proxyman.command.command_pb2 import AddInboundRequest
from app.proxyman.config_pb2   import ReceiverConfig
from config_pb2 import InboundHandlerConfig
from app.proxyman.command.command_pb2_grpc import HandlerServiceStub
from common.net.port_pb2 import PortRange
from common.net.address_pb2 import IPOrDomain
from google.protobuf.any_pb2 import Any
import grpc

# Create a channel and a stub
channel = grpc.insecure_channel('localhost:62789')
stub = HandlerServiceStub(channel)

inbound_setting = Any()
inbound_setting.Pack(
        ReceiverConfig(
            port_range=PortRange(From=9000, To=9020),
            listen=IPOrDomain(domain='localhost')
            )
        )
print(
        stub.AddInbound(
            AddInboundRequest(
                inbound=InboundHandlerConfig(
                    tag='amir',
                    receiver_settings=inbound_setting,
                    proxy_settings=Any()
                    )
                )
            )
        )


