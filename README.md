## V2ray Health Probe

$${\color{red}PROBE \color{blue}-> [REQ] -> [PROXY] -> \color{green}[Instagram, Whatsapp, Google] \color{blue}-> [RESPONSE] -> \color{red}PROBE -> (InfluxDB)}$$ 


### Step To Setup

1 - Add config (Vmess supported At the Moment) to `config/` with prefix of `test_` (up to 10 config, the limitation is port if you need test it externally)

2 - Setup docker-compose

3 - Run it `python main.py`

4 - Check the InfluxDB dashboard
