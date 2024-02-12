import asyncio
import os
import json
import aiohttp
import time
from typing import Dict, List, Optional


_DEFAULT_CONFIG = 'default_config.json'
_FINAL_CONFIG = 'config.json'
_IGNORE_LIST = [_FINAL_CONFIG, 'sample_config.json']
_BEGIN_PORT = 5001


class Config:

    def get_port(self):
        raise NotImplemented


class VmessConfig(Config):

    def __init__(self, config):
        self.config = config
    
    def get_port(self):
        return self.config['settings']['vnext'][0]['port']


_PROTOCOL_MAPPING = {
        'vmess' : VmessConfig
        }


class TestClient:
    def __init__(self, outbound, tag=None, port=None):
        self.tag = tag if tag else outbound['tag']
        self.port = port if port else _PROTOCOL_MAPPING[outbound['protocol']](outbound).get_port()
        self.outbounds = outbound
        self.session = aiohttp.ClientSession()
        self.protocol = outbound['protocol']

    def outbound_json_config(self) -> Dict:
        return self.outbounds

    def inbound_json_config(self) -> Dict:
        return {
            "listen" : "0.0.0.0",
            "port": self.port,
            "tag": self.tag,
            "protocol": "http",
            "settings": {}
            }

    def rule_json_config(self) -> Dict:
        return {
                "type": "field",
                "inboundTag": [self.tag],
                "outboundTag": self.tag
                }

    # Time is in miliseconds
    async def get(self, url='google.com', timeout=2) -> Optional[float]:
        start = time.time()
        try:
            await self.session.get(url, proxy="http://localhost:{}".format(self.port), timeout=timeout)
        except asyncio.exceptions.TimeoutError:
            return None
        return (time.time() - start)  * 1000

    def __repr__(self) -> str:
        return f"Client tag: {self.tag}"

def generate_config_create_clients() -> List[TestClient]:
    configs = {}
    for file in os.listdir('config'):
        if file in _IGNORE_LIST:
            continue

        with open('config/' + file, 'r') as config:
            configs[file] = json.load(config)

    v2ray_config = configs[_DEFAULT_CONFIG]
    del configs[_DEFAULT_CONFIG]

    proxy_list = []
    i = _BEGIN_PORT
    for _ , config in configs.items():
        proxy_list.append(TestClient(config, port=i))
        i += 1

    v2ray_config['outbounds'].extend([config.outbound_json_config() for config in proxy_list])
    v2ray_config['inbounds'].extend([config.inbound_json_config() for config in proxy_list])
    v2ray_config['routing']['rules'].extend([config.rule_json_config() for config in proxy_list])
    with open('config/' + _FINAL_CONFIG, 'w+') as f:
        json.dump(v2ray_config, f)
    return proxy_list
