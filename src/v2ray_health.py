import os
import json
from aiohttp import request

_DEFAULT_CONFIG = 'default_config.json'

def generate_config():
    outbound_configs = {}
    for file in os.listdir('config'):
        with open('config/' + file, 'r') as config:
            outbound_configs[file] = json.load(config)
    print(outbound_configs)

