from app.stats.command.command_pb2_grpc import StatsServiceStub
from app.stats.command.command_pb2 import SysStatsRequest
import grpc


# Create a channel and a stub
channel = grpc.insecure_channel('localhost:62789')
stub = StatsServiceStub(channel)

print(stub.GetSysStats(SysStatsRequest()))


