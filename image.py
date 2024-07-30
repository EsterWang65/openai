import os
import requests
import json
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = "https://gjun-open-ai.openai.azure.com/"
deployment = "Dalle3"
key = "8b6041cc25f54c05b5e7629715225837"
      
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=key,
    api_version="2024-02-01",
)

result = client.images.generate(
    model=deployment, 
    prompt="兩隻狗在玩泥巴",
    n=1
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']

print(image_url)