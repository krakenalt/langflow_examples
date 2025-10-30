import os

import requests
from dotenv import load_dotenv
flow_id = "FLOW_ID from uv run command"
load_dotenv()
url = f"http://127.0.0.1:8001/flows/{flow_id}/run?x-api-key={os.environ.get('LANGFLOW_API_KEY')}"


resp = requests.post(url, json={"input_value": "Привет как дела?"})

print(resp.json())