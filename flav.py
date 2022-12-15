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
flavors_url = f"{env_url}:8774/v2.1/flavors"
flavors_response = requests.get(flavors_url, headers={"X-Auth-Token": token_id})
flavors_response.raise_for_status()
flavors = flavors_response.json()

fi = 0
flav_name = {}

for flavor in flavors["flavors"]:
    fi += 1
    flav_name[fi] = flavor["name"]
    print(fi, flavor["name"])

with open("flavors.pkl", "wb") as f:
    pickle.dump(flav_name, f)