

from kaggle_secrets import UserSecretsClient
user_secrets = UserSecretsClient()
secret_value_0 = user_secrets.get_secret("API")
secret_value_1 = user_secrets.get_secret("API_URL")
secret_value_2 = user_secrets.get_secret("text_api")

import requests

API_URL = secret_value_1
headers = {"Authorization": secret_value_0}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content
image_bytes = query({
    "inputs": "Astronaut riding a horse"
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))