from influxdb_client import Point
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync


class MonitoringClient:
    def __init__(self, url, token, bucket, org, prob_name):
        self._influxdb_client = InfluxDBClientAsync(url=url, token=token)
        self._write_api = self._influxdb_client.write_api()
        self._bucket = bucket
        self._prob_name = prob_name
        self._org = org

    async def send_point(self, node_tag: str, destination: str, protocol: str, response_time: float):
        point = Point("latency")
        point.tag('prob_name', self._prob_name)
        point.tag('node', node_tag)
        point.tag('destination', destination)
        point.tag('protcol', protocol)
        point.field("response_time", response_time)
        await self._write_api.write(bucket=self._bucket, org=self._org, record=point)

    async def __aexit__(self, *args):
        await self._influxdb_client.close()
