import ipaddress
import ipaddress
import json
ips = []

asset_value=['92.45.88.56/29','92.45.88.96/27','176.235.254.192/27','176.236.137.40/29','213.14.79.208/28','213.14.123.112/28','213.74.138.32/30','213.74.138.44/30','213.74.195.200/29','213.74.195.224/27','213.74.196.0/25','213.74.197.8/30','213.74.197.208/29']
ip_list = []
ips = []
for i in asset_value:


    net = ipaddress.ip_network(i)
    for x in net:
        ips.append(str(x))

with open('test_out.json', 'w') as f:
    json.dump(ips, f, indent=1)


