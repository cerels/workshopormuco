import pickle
import requests
import json
import subprocess

# Import the token and token_id values from the file using the pickle module
subprocess.run(["python", "auth.py"])
with open("tokens.pkl", "rb") as f:
    token = pickle.load(f)
    token_id = pickle.load(f)

# Image list request
glance_port = "9292"
headers = {"X-Auth-Token": token_id}

env_url = "https://api-uat-001.ormuco.com"
response = requests.get(url=f"{env_url}:{glance_port}/v2/images", headers=headers)
images = response.json()

i = 0
OS_name = {}

for image in images['images']:
    i += 1
    OS_name[i] = image["name"]
    print(i, image["name"])

with open("images.pkl", "wb") as f:
    pickle.dump(OS_name, f)


