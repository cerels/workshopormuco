import pickle
import requests
import json
import subprocess

# Import the token and token_id values from the file using the pickle module
subprocess.run(["python", "auth.py"])
with open("tokens.pkl", "rb") as f:
    token = pickle.load(f)
    token_id = pickle.load(f)

# Network list request
neutron_port = "9696"
headers = {"X-Auth-Token": token_id}

env_url = "https://api-uat-001.ormuco.com"
response = requests.get(url=f"{env_url}:{neutron_port}/v2.0/networks", headers=headers)
networks = response.json()

ni = 0
net_name = {}

for network in networks['networks']:
    ni += 1
    net_name[ni] = network["name"]
    print(ni, network["name"])

with open("networks.pkl", "wb") as f:
    pickle.dump(net_name, f)



