# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from app.observatory.command import command_pb2 as app_dot_observatory_dot_command_dot_command__pb2


class ObservatoryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetOutboundStatus = channel.unary_unary(
                '/v2ray.core.app.observatory.command.ObservatoryService/GetOutboundStatus',
                request_serializer=app_dot_observatory_dot_command_dot_command__pb2.GetOutboundStatusRequest.SerializeToString,
                response_deserializer=app_dot_observatory_dot_command_dot_command__pb2.GetOutboundStatusResponse.FromString,
                )


class ObservatoryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetOutboundStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ObservatoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetOutboundStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOutboundStatus,
                    request_deserializer=app_dot_observatory_dot_command_dot_command__pb2.GetOutboundStatusRequest.FromString,
                    response_serializer=app_dot_observatory_dot_command_dot_command__pb2.GetOutboundStatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'v2ray.core.app.observatory.command.ObservatoryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ObservatoryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetOutboundStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v2ray.core.app.observatory.command.ObservatoryService/GetOutboundStatus',
            app_dot_observatory_dot_command_dot_command__pb2.GetOutboundStatusRequest.SerializeToString,
            app_dot_observatory_dot_command_dot_command__pb2.GetOutboundStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
