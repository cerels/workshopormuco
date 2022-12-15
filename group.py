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


groups_url = f"{env_url}:9696/v2.0/security-groups"
groups_response = requests.get(groups_url, headers={"X-Auth-Token": token_id})
groups_response.raise_for_status()
groups = groups_response.json()

gi = 0
group_name = {}

for group in groups["security_groups"]:
    gi += 1
    group_name[gi] = group["name"]
    print(gi, group["name"])

with open("group.pkl", "wb") as f:
    pickle.dump(group_name, f)