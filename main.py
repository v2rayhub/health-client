import time
import asyncio
from configparser import ConfigParser
from src.influx_client import MonitoringClient 

config = ConfigParser()
config.read('./config.toml')
influx_config = config["influxdb"]



async def main():
    client = MonitoringClient(
            url=influx_config['url'],
            token=influx_config['token'],
            bucket=influx_config['bucket'],
            org=influx_config['org'],
            prob_name=config['app']['prob_name']
            )
    for i in range(10):
        await client.send_point('test', 'http', i * 0.1)
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())
