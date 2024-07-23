import os
import requests
import json
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = os.getenv("ENDPOINT_URL", "https://gjun-oai-user04.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "GPT")
key = "2566bf641510460fafe5c4145bc80955"

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default")
      
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key = key,
    api_version="2024-05-01-preview",
)

prompt = input("請輸入您的問題：")
while prompt != "":
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
    prompt = input("請輸入您的問題：")