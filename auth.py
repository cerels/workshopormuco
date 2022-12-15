import requests
import pickle
import subprocess

payload = {
    "auth": {
        "identity": {
            "methods": ["password"],
            "password": {
                "user": {
                    "name": "workshop2022@utb.edu.co",
                    "domain": {"name": "Default"},
                    "password": "ILOVECLOUD2022",
                }
            },
        }
    }
}

env_url = "https://api-uat-001.ormuco.com"
url_token = env_url + ":5000/v3/auth/tokens"

# 1. Authentication requests
token = requests.post(url=url_token, json=payload)
token_id = token.json().get("token").get("id")

# Save the token and token_id values to a file using the pickle module
with open("tokens.pkl", "wb") as f:
    pickle.dump(token, f)
    pickle.dump(token_id, f)