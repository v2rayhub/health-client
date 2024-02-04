import asyncio
from configparser import ConfigParser
from src.influx_client import MonitoringClient 
from src.v2ray_health import generate_config_create_clients

HOSTS = [
        'https://www.instagram.com',
        'https://www.google.com',
        'https://www.whatsapp.com/'
        ]

config = ConfigParser()
config.read('./config.toml')
influx_config = config["influxdb"]


async def main():
    clients = generate_config_create_clients()
    monitoring_client = MonitoringClient(
            url=influx_config['url'],
            token=influx_config['token'],
            bucket=influx_config['bucket'],
            org=influx_config['org'],
            prob_name=config['app']['prob_name']
            )
    while True:
        for client in clients:
            for url in HOSTS:
                response_time = await client.get(url)
                await monitoring_client.send_point(client.tag, url, client.protocol, response_time)
        await asyncio.sleep(int(config['app'].get('sampling_time', '10')))



if __name__ == '__main__':
    asyncio.run(main())
