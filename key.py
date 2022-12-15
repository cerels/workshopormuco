import pickle
import requests
import json
import subprocess
# Import the token and token_id values from the file using the pickle module
subprocess.run(["python", "auth.py"])
with open("tokens.pkl", "rb") as f:
    token = pickle.load(f)
    token_id = pickle.load(f)
env_url = "https://api-uat-001.ormuco.com"


keys_url = f"{env_url}:8774/v2.1/os-keypairs"
keys_response = requests.get(keys_url, headers={"X-Auth-Token": token_id})
keys_response.raise_for_status()
keys = keys_response.json()

ki = 0
key_name = {}

for key in keys["keypairs"]:
    ki += 1
    key_name[ki] = key["keypair"]["name"]
    print(ki, key["keypair"]["name"])

with open("key.pkl", "wb") as f:
    pickle.dump(key_name, f)