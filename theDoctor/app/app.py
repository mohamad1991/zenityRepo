import os
import requests

code_name = os.getenv("CODE_NAME", "theDoctor")

try:
    res = requests.post("http://127.0.0.1:5000/secret", json={"codeName": code_name})
    print("Response:", res.status_code, res.text)
except Exception as e:
    print("Failed to send codeName:", e)
