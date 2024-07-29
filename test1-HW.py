import os
import requests
import json
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = "https://gjun-oai-user01.openai.azure.com/"
deployment = "GPT"
key = "6652e17debe84a8d8fc8f529c6edefdb"
      
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=key,
    api_version="2024-05-01-preview",
)

prompt = input("請輸入您的問題：")

completion = client.chat.completions.create(
    model=deployment,
    messages= [
    {
      "role": "user",
      "content": prompt
    }],
    max_tokens=800,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
)
print(completion.choices[0].message.content)