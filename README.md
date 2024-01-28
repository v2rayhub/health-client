Generate protos from:

```
git clone git@github.com:v2fly/v2ray-core.git
git checkout v5.13.0
python3 -m grpc_tools.protoc -I. --python_out=../v2ray-health-client --grpc_python_out=../v2ray-health-client app/proxyman/config.proto
python3 -m grpc_tools.protoc -I. --python_out=../v2ray-health-client --grpc_python_out=../v2ray-health-client app/stats/command/command.proto
python3 -m grpc_tools.protoc -I. --python_out=../v2ray-health-client --grpc_python_out=../v2ray-health-client common/protoext/extensions.proto
```

Alternatively to generate all(useless)
```
find . -name '*.proto' | xargs -I % python3 -m grpc_tools.protoc -I. --python_out=../v2ray-health-client --grpc_python_out=../v2ray-health-client %
```

Sample

```
python get_system_stats.py
```
