import asyncio
from configparser import ConfigParser
from src.influx_client import MonitoringClient 
from src.v2ray_health import generate_config_create_clients
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

LOGGER = logging.getLogger(__name__)

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
    LOGGER.info('Start with {} nodes'.format(len(clients)))
    monitoring_client = MonitoringClient(
            url=influx_config['url'],
            token=influx_config['token'],
            bucket=influx_config['bucket'],
            org=influx_config['org'],
            prob_name=config['app']['prob_name']
            )
    while True:
        try:
            tasks = []
            for client in clients:
                for url in HOSTS:
                    async def fetch(client, url, monitoring_client):
                        try:
                            response_time = await client.get(url, 1)
                        except Exception as e:
                            LOGGER.error("Error in checking url %s with node %s", url, client)
                            LOGGER.exception(e)
                            return
                        LOGGER.info("Going to check %s through node %s, response_time %s", url, client, response_time)
                        if response_time is None:
                            return
                        await monitoring_client.send_point(client.tag, url, client.protocol, response_time)
                    tasks.append(asyncio.create_task(fetch(client, url , monitoring_client)))
            asyncio.gather(*tasks)
            await asyncio.sleep(int(config['app'].get('sampling_time', '10')))
        except Exception as e:
            LOGGER.exception(e)


if __name__ == '__main__':
    asyncio.run(main())
