FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y wget unzip
RUN wget https://github.com/v2fly/v2ray-core/releases/latest/download/v2ray-linux-64.zip
RUN unzip v2ray-linux-64.zip -d /usr/local/bin/
RUN rm v2ray-linux-64.zip
RUN mv /usr/local/bin/systemd/system/v2ray.service /etc/systemd/system/v2ray_probe
COPY . /app
RUN mkdir /usr/local/etc/v2ray
RUN mv /app/config/config.json /usr/local/etc/v2ray/
COPY v2ray_probe.service /etc/systemd/system/v2ray_probe.service

CMD ["/bin/bash", "-c", "systemctl enable v2ray_probe.service && systemctl start v2ray_probe.service && systemctl enable v2ray.service && systemctl start v2ray.service"]

