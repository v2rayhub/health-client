## V2ray Health Probe

Probe -> [REQ] -> [PROXY] -> [Instagram, Whatsapp, Google] -> [RESPONSE] -> Probe -> (InfluxDB)

### Step To Setup

1 - Add config (Vmess supported At the Moment) to `config/` with prefix of `test_` (up to 10 config, the limitation is port if you need test it externally)

2 - Setup docker-compose

3 - Run it `python main.py`

4 - Check the InfluxDB dashboard
