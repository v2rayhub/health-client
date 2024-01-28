Generate protos from:

```
git clone git@github.com:v2fly/v2ray-core.git
git checkout v5.13.0
find . -name '*.proto' | xargs -I % python3 -m grpc_tools.protoc -I. --python_out=../v2ray-health-client --grpc_python_out=../v2ray-health-client %
```

Sample

```
python get_system_stats.py
```


## TODO:

- Add graph viz
- Add monitoring per node
